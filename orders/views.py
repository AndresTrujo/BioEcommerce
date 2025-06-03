from django.shortcuts import render, redirect, get_object_or_404
# Importa settings para acceder a las claves de Stripe
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
# Necesario para webhooks, cuidado con esto
from django.views.decorators.csrf import csrf_exempt

import stripe  # Importa la librería de Stripe

from cart.models import Cart
from orders.models import Order, OrderItem
from .forms import OrderCreateForm


def order_create(request):
    cart = None
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return redirect('cart:cart_detail')

        if not cart.items.exists():
            return redirect('cart:cart_detail')
    else:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderCreateForm(request.POST, initial={
                'full_name': request.user.get_full_name() if hasattr(request.user, 'get_full_name') else request.user.username,
                'email': request.user.email,
                'address': getattr(request.user, 'address', '')
            })
        else:
            form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)

            if request.user.is_authenticated:
                order.user = request.user

            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.PROD_PRECIO_PUB,
                    quantity=item.quantity
                )

            # TODO: Guardamos la orden, pero no la borramos del carrito ni la sesión aún.
            # Esto lo haremos DESPUÉS de un pago exitoso con Stripe.
            # Almacenamos el ID de la orden en la sesión para usarlo en la vista de pago
            request.session['order_id'] = order.id

            # Redirigir a la vista de procesamiento de pago de Stripe
            return redirect('orders:payment_process')
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm(initial={
                'full_name': request.user.get_full_name() if hasattr(request.user, 'get_full_name') else request.user.username,
                'email': request.user.email,
                'address': getattr(request.user, 'address', '')
            })
        else:
            form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {
        'form': form,
        'cart': cart
    })


def payment_process(request):
    cart_id = request.session.get('cart_id')
    order_id = request.session.get('order_id', None)
    cart = Cart.objects.get(id=cart_id)
    if not order_id:
        return redirect('cart:cart_detail')  # O a una página de error

    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # Crear los ítems para la sesión de Checkout de Stripe
        line_items = []
        for item in order.items.all():
            line_items.append({
                'price_data': {
                    'currency': 'mxn',  # O la moneda que uses
                    'product_data': {
                        'name': item.product.PROD_NOMBRE,  # Asumiendo que tu producto tiene un nombre
                    },
                    # Stripe espera el precio en centavos
                    'unit_amount': int(item.price * 100),
                },
                'quantity': item.quantity,
            })

        try:
            # Crear la sesión de Checkout de Stripe
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('orders:payment_success')),
                cancel_url=request.build_absolute_uri(
                    reverse('orders:payment_canceled')),
                # Opcional: pasar el ID de la orden como metadata
                metadata={
                    'order_id': order.id
                }
            )
            if 'cart_id' in request.session:
                cart.delete()
                del request.session['cart_id']
            if 'order_id' in request.session:
                del request.session['order_id']
            # Redirigir al usuario a la URL de la sesión de Checkout
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            # Manejar errores de Stripe
            # Debes crear esta plantilla
            return render(request, 'orders/payment_error.html', {'error': str(e)})
    else:
        # Renderizar una plantilla de confirmación de pago antes de redirigir a Stripe
        # O podrías simplemente redirigir a POST directamente si el usuario ya ha confirmado la orden
        cart.delete()
        del request.session['cart_id']
        return render(request, 'orders/payment_process.html', {'order': order})


def payment_success(request):
    # Esta vista solo se alcanza si el usuario es redirigido por Stripe.
    # La confirmación final del pago debe hacerse a través de un webhook.
    # Aquí podríamos mostrar un mensaje de "Gracias por tu compra".

    order_id = request.session.get('order_id', None)
    if order_id:
        # Opcional: Marcar la orden como pagada aquí si el webhook no es indispensable en tu caso
        # Sin embargo, el webhook es más robusto para esto.
        order = get_object_or_404(Order, id=order_id)
        if not order.paid:
            order.paid = True
            order.save()

        # Limpiar la sesión después de que la orden haya sido procesada
        if 'cart_id' in request.session:
            del request.session['cart_id']
        if 'order_id' in request.session:
            del request.session['order_id']

        return render(request, 'orders/payment_success.html')
    # O a tu página de inicio si no hay order_id
    return redirect('cart:cart_detail')


def payment_canceled(request):
    # El usuario canceló el pago, puedes redirigirlo de vuelta al carrito o a la página de la orden
    return render(request, 'orders/payment_canceled.html')


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})


@csrf_exempt  # Deshabilitar CSRF para esta vista, ya que Stripe no envía token CSRF
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Manejar el evento
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Recuperar el ID de la orden de la metadata de la sesión
        order_id = session.get('metadata', {}).get('order_id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                if not order.paid:  # Marcar la orden como pagada solo si no lo está ya
                    order.paid = True
                    order.save()
                    # Aquí podrías enviar un correo de confirmación, actualizar el stock, etc.
                    print(f"Order {order_id} marked as paid by webhook.")

                    # Opcional: Si el carrito aún existe y no ha sido borrado en `payment_success`, bórralo aquí
                    # Es más seguro que el carrito se borre en la confirmación del webhook.
                    # Puedes pasar el cart_id en la metadata de la sesión de Stripe si lo necesitas.
                    # Por simplicidad, asumimos que ya se manejó en payment_success o que no necesitas borrarlo aquí
                    # si el webhook es el único punto de confirmación.
                    # Si quieres borrar el carrito aquí, necesitarías pasar el cart_id en la metadata de la sesión de Stripe
                    # y luego recuperarlo.

            except Order.DoesNotExist:
                print(f"Order with ID {order_id} not found for webhook event.")
        else:
            print("No order_id found in webhook metadata.")

    # Puedes manejar otros tipos de eventos aquí si es necesario
    # elif event['type'] == 'payment_intent.succeeded':
    #     payment_intent = event['data']['object']
    #     print(f"PaymentIntent succeeded: {payment_intent['id']}")

    return HttpResponse(status=200)  # Importante: Devolver un 200 OK a Stripe

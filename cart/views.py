from django.shortcuts import render
from products.models import Producto
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.


def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    product = get_object_or_404(Producto, ID_PRODUCTO=product_id)
    category = product.PROD_CATEGORIA
    category_slug = category.CAT_SLUG
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, "Producto añadido al carrito")
    return redirect('products:product_detail', id=product_id)


def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    if not cart or not cart.items.exists():
        cart = None

    context = {
        'cart': cart,
    }

    return render(request, 'cart/detail.html', context)


def cart_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(
        CartItem, cart=cart, product__ID_PRODUCTO=product_id)
    item.delete()

    return redirect('cart:cart_detail')


@require_POST
def cart_item_add(request, product_id):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return JsonResponse({'error': 'No cart found'}, status=404)

    cart = get_object_or_404(Cart, id=cart_id)
    product = get_object_or_404(Producto, ID_PRODUCTO=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return JsonResponse({'quantity': cart_item.quantity, 'item_total': cart_item.get_total_price(), 'total': cart.get_total_price()})


@require_POST
def cart_item_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return JsonResponse({'error': 'No cart found'}, status=404)

    cart = get_object_or_404(Cart, id=cart_id)
    product = get_object_or_404(Producto, ID_PRODUCTO=product_id)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return JsonResponse({'quantity': cart_item.quantity, 'total': cart.get_total_price()})
        else:
            cart_item.delete()
            return JsonResponse({'quantity': 0, 'removed': True, 'total': cart.get_total_price()})
    except CartItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

from django.shortcuts import render
from products.models import Producto
from cart.models import Cart_Model, Cart_Item
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.

"""Añade un producto al carrito"""
def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart_Model.objects.get(id=cart_id)
        except Cart_Model.DoesNotExist:
            cart = Cart_Model.objects.create()
    else:
        cart = Cart_Model.objects.create()
        request.session['cart_id'] = cart.id

    product = get_object_or_404(Producto, ID_PRODUCTO=product_id)
    category = product.PROD_CATEGORIA
    category_slug = category.CAT_SLUG
    cart_item, created = Cart_Item.objects.get_or_create(
        cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, "Producto añadido al carrito")
    return redirect('products:product_detail', id=product_id)

"""Renderiza el detalle del carrito de compras"""
def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart_Model, id=cart_id)
    if not cart or not cart.items.exists():
        cart = None

    context = {
        'cart': cart,
    }

    return render(request, 'cart/detail.html', context)

"""Elimina un producto del carrito"""
def cart_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart_Model, id=cart_id)
    item = get_object_or_404(
        Cart_Item, cart=cart, product__ID_PRODUCTO=product_id)
    item.delete()

    return redirect('cart:cart_detail')

"""Requiere post para añadir un item al carrito en la sección de cart detail."""
@require_POST
def cart_item_add(request, product_id):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return JsonResponse({'error': 'No cart found'}, status=404)

    cart = get_object_or_404(Cart_Model, id=cart_id)
    product = get_object_or_404(Producto, ID_PRODUCTO=product_id)

    cart_item, created = Cart_Item.objects.get_or_create(
        cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return JsonResponse({'quantity': cart_item.quantity, 'item_total': cart_item.get_total_price(), 'total': cart.get_total_price()})


"""Elimina un item del carrito en la sección de cart detail."""
@require_POST
def cart_item_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return JsonResponse({'error': 'No cart found'}, status=404)

    cart = get_object_or_404(Cart_Model, id=cart_id)
    product = get_object_or_404(Producto, ID_PRODUCTO=product_id)

    try:
        cart_item = Cart_Item.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return JsonResponse({'quantity': cart_item.quantity, 'total': cart.get_total_price()})
        else:
            cart_item.delete()
            return JsonResponse({'quantity': 0, 'removed': True, 'total': cart.get_total_price()})
    except Cart_Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

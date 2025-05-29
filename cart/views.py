from django.shortcuts import render
from products.models import Producto
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.
@require_POST
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
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    
    return redirect('products:product_list_by_category', category_slug=category_slug)

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None
    
    if cart_id:
        try:
            cart = get_object_or_404(Cart, id=cart_id)
        except Cart.DoesNotExist:
            cart = None
    
    context = {
        'cart': cart,
    }
    
    return render(request, 'cart/detail.html', context)

def cart_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, cart=cart, product__ID_PRODUCTO=product_id)
    item.delete()
    
    return redirect('cart:cart_detail')
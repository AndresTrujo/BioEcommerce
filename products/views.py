from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Categoria, Producto
from random import choice


def last_page_redirect(request):
    last_page = request.session.get('last_page', '/')
    return redirect(last_page)


def landing_page(request):
    request.session['last_page'] = request.get_full_path()
    template_name = 'products/index.html'
    lista_productos = Producto.objects.filter(PROD_NOMBRE__contains='CREATINA')[:3]
    context = {
        "products": lista_productos,
    }
    return render(request, template_name, context)


def product_list(request, category_slug=None):
    request.session['last_page'] = request.get_full_path()
    category = None
    products = Producto.objects.filter(PROD_DISPONIBLE=True)
    categories = Categoria.objects.all()
    rand_cat = choice(categories)
    first_three = Producto.objects.filter(PROD_CATEGORIA=rand_cat)[:3]
    if category_slug:
        category = get_object_or_404(Categoria, CAT_SLUG=category_slug)
        products = products.filter(PROD_CATEGORIA=category)

    return render(request, 'products/product/list.html', context={
        'rand_cat': rand_cat,
        'category': category,
        'products': products,
        'categories': categories,
        'first_three': first_three
    })
# views.py
# TODO: Este es un comentario para verificar cambios


def product_detail(request, id):
    product = get_object_or_404(Producto, ID_PRODUCTO=id, PROD_DISPONIBLE=True)
    categories = Categoria.objects.all()
    rand_cat = choice(categories)
    first_three = Producto.objects.filter(PROD_CATEGORIA=rand_cat)[:3]
    if not product:
        print("El Producto no fue encontrado")
    return render(request, 'products/product/detail.html', {'product': product, 'first_three': first_three, 'rand_cat': rand_cat, 'categories': categories})

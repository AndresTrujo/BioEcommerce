from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from random import choice


def landing_page(request):
    template_name = 'products/index.html'
    lista_productos = Producto.objects.all()[:3]
    context = {
        "products": lista_productos,
    }
    return render(request, template_name, context)


def product_list(request, category_slug=None):
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


def product_detail(request, id):
    product = get_object_or_404(Producto, ID_PRODUCTO=id, PROD_DISPONIBLE=True)
    if not product:
        print("El Producto no fue encontrado")
    return render(request, 'products/product/detail.html', {'product': product})

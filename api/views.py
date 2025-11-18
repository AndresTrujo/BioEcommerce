from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Categoria, Producto
from .serializers import ProductoSerializer


class ProductoView(APIView):
    def get(self, request):
        # placeholder: puedes usar tu propia imagen en /static/img/placeholder.jpg
        # o cambiar a un placeholder externo si prefieres (ej. via.placeholder.com)
        default_placeholder = request.build_absolute_uri('/static/img/placeholder.jpg')
        products = []
        for p in Producto.objects.all():
            # resolver URL de imagen de forma segura; algunos objetos FileField lanzan
            # ValueError cuando no tienen archivo asociado
            try:
                if p.PROD_IMAGEN and getattr(p.PROD_IMAGEN, 'name', None):
                    image_url = request.build_absolute_uri(p.PROD_IMAGEN.url)
                else:
                    image_url = default_placeholder
            except ValueError:
                image_url = default_placeholder

            prod = {
                "ID_PRODUCTO": p.ID_PRODUCTO,
                "PROD_NOMBRE": p.PROD_NOMBRE,
                "PROD_PRECIO_PUB": p.PROD_PRECIO_PUB,
                "PROD_CATEGORIA": p.PROD_CATEGORIA.CAT_NOMBRE if p.PROD_CATEGORIA else None,
                "PROD_IMAGEN": image_url,
            }
            products.append(prod)

        return Response(products)
    

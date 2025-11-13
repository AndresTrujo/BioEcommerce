from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Categoria, Producto
from .serializers import ProductoSerializer

class ProductoView(APIView):
    def get(self, request):
        output = [{"ID_PRODUCTO": p.ID_PRODUCTO, "PROD_NOMBRE": p.PROD_NOMBRE, "PROD_PRECIO_PUB": p.PROD_PRECIO_PUB, "PROD_CATEGORIA_":p.PROD_CATEGORIA.CAT_NOMBRE} for p in Producto.objects.all()]
        return Response(output)
    

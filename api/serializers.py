from rest_framework import serializers
from products.models import Producto, Categoria

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['ID_PRODUCTO', 'PROD_NOMBRE', 'PROD_PRECIO_PUB', 'PROD_IMAGEN', 'PROD_DISPONIBLE', 'PROD_GRAMAJE', 'PROD_CATEGORIA']
        read_only_fields = ['ID_PRODUCTO']
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['CAT_NOMBRE', 'CAT_SLUG']
        
from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "CAT_NOMBRE", "CAT_SLUG"]
    prepopulated_fields = {"CAT_SLUG": ("CAT_NOMBRE",)}
    
@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["ID_PRODUCTO", "PROD_NOMBRE", "PROD_PRECIO_MAY", "PROD_PRECIO_PUB", "PROD_CREADO", "PROD_MODIFICADO", "PROD_CATEGORIA", "PROD_DISPONIBLE"]
    
    prepopulated_fields = {'PROD_SLUG':('PROD_NOMBRE',)}
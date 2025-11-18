from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Producto


# @method_decorator(cache_page(60*5), name='dispatch')
class ProductoView(APIView):
    def get(self, request):
        qs = Producto.objects.select_related('PROD_CATEGORIA').all()
        # values() devuelve solo los campos que necesitamos (evita cargar objetos completos)
        rows = qs.values('ID_PRODUCTO', 'PROD_NOMBRE', 'PROD_PRECIO_PUB', 'PROD_CATEGORIA__CAT_NOMBRE', 'PROD_IMAGEN')
        # mapear los nombres para mantener compatibilidad con el frontend
        output = []
        base = request.build_absolute_uri('/')[:-1]  # http://host:port
        for r in rows:
            img = r.get('PROD_IMAGEN')
            # si PROD_IMAGEN es ruta relativa, conviértela en absoluta; si es None usar placeholder
            image_url = request.build_absolute_uri(img) if img else request.build_absolute_uri('/static/img/placeholder.png')
            output.append({
                'ID_PRODUCTO': r['ID_PRODUCTO'],
                'PROD_NOMBRE': r['PROD_NOMBRE'],
                'PROD_PRECIO_PUB': r['PROD_PRECIO_PUB'],
                'PROD_CATEGORIA': r.get('PROD_CATEGORIA__CAT_NOMBRE'),
                'PROD_IMAGEN': image_url,
            })
        return Response(output)
    

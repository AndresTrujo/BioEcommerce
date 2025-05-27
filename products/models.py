from django.db import models
from django.urls import reverse
# Create your models here


class Categoria(models.Model):
    CAT_NOMBRE = models.CharField(max_length=50)
    CAT_SLUG = models.SlugField(default="", null=False, unique=True)

    class Meta:
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.CAT_NOMBRE
    
class Producto(models.Model):
    ID_PRODUCTO = models.CharField(primary_key=True, max_length=50)
    PROD_CATEGORIA = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)
    PROD_NOMBRE = models.CharField(max_length=50)
    PROD_DESCRIPCION = models.CharField(max_length=50, blank=True)
    PROD_SLUG = models.SlugField(max_length=250)
    CONTENIDO_PZS = models.CharField(max_length=50, blank=True)
    PROD_PRECIO_MAY = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    PROD_PRECIO_PUB = models.DecimalField(max_digits=10, decimal_places=2)
    PROD_DISPONIBLE = models.BooleanField(default=True)
    PROD_GRAMAJE = models.FloatField(null=True, blank=True)
    PROD_IMAGEN = models.ImageField(upload_to='productos/', null=True, blank=True)
    PROD_CREADO = models.DateTimeField(auto_now_add=True)
    PROD_MODIFICADO = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.PROD_NOMBRE
    
    def get_absolute_url(self):
        return reverse("productos:detalle_producto", kwargs={"id": self.id, "slug": self.PROD_SLUG})
    
    

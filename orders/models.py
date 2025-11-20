from django.db import models
from products.models import Producto
from django.conf import settings


class Order_Model(models.Model):
    USER= models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,  # O models.CASCADE, dependiendo de tu lógica
                             null=True, blank=True,  # Puede ser null si el usuario no está autenticado
                             related_name='orders')

    FULL_NAME = models.CharField(max_length=255)
    EMAIL = models.EmailField()
    ADDRESS = models.CharField(max_length=150)
    TOTAL = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PAYMENT_INTENT_ID = models.CharField(max_length=255, null=True, blank=True)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)
    PAID = models.BooleanField(default=False)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class Order_Item(models.Model):
    ORDER = models.ForeignKey(
        Order_Model, related_name='items', on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(
        Producto, related_name='order_items', on_delete=models.CASCADE)
    PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    QUANTITY = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.PRICE * self.QUANTITY
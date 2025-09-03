from django.db import models
from products.models import Producto


class Cart_Model(models.Model):
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class Cart_Item(models.Model):
    CART = models.ForeignKey(Cart_Model, related_name='items', on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Producto, related_name='cart_items', on_delete=models.CASCADE)
    QUANTITY = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.PRODUCT.PROD_PRECIO_PUB * self.QUANTITY
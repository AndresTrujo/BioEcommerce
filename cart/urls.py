from django.urls import path
from .views import cart_add, cart_detail, cart_remove, cart_item_add, cart_item_remove

app_name = 'cart'
urlpatterns = [

    path('', cart_detail, name='cart_detail'),
    path('add/<str:product_id>/', cart_add, name='cart_add'),
    path('remove/<str:product_id>/', cart_remove, name='cart_remove'),
    path('item/add/<str:product_id>/', cart_item_add, name='cart_item_add'),
    path('item/remove/<str:product_id>/',
         cart_item_remove, name='cart_item_remove'),
]
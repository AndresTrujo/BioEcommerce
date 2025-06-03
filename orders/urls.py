from django.urls import path
from .views import order_create, order_confirmation, payment_process, payment_success, payment_canceled, stripe_webhook, buy_now

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'), 
    path('process/', payment_process, name='payment_process'), # Nueva URL para el proceso de pago
    path('completed/', payment_success, name='payment_success'), # Nueva URL para el éxito del pago
    path('canceled/', payment_canceled, name='payment_canceled'), # Nueva URL para el pago cancelado
    path('confirmation/<int:order_id>', order_confirmation, name='order_confirmation'),
    path('buy_now/<str:product_id>/', buy_now, name='buy_now'),  # Nueva URL para comprar ahora
    path('webhook/', stripe_webhook, name='stripe_webhook'),
]

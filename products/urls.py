from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('products/', views.product_list, name="product_list"),
    path('products/<slug:category_slug>', views.product_list, name="product_list_by_category"),
    path('product/<str:id>/', views.product_detail, name="product_detail")
]

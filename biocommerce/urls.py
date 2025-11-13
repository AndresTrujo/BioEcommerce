from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
# Asegúrate de cambiar 'tu_app' por el nombre real de tu aplicación (ej. users.views)

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ADDED
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ADDED
    path('api/', include('api.urls')),  # ADDED: central API app / router
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    path('chatbot/', include('chatbot.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductoView,
    UserListView,
    UserDetailView,
    RegisterView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    ChangePasswordView,
    create_order_checkout,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('products/', ProductoView.as_view(), name='producto-list'),

    # Auth / users
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/password/reset/', PasswordResetRequestView.as_view(), name='auth-password-reset'),
    path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='auth-password-reset-confirm'),
    path('auth/password/change/', ChangePasswordView.as_view(), name='auth-password-change'),
    path('orders/create-checkout/', create_order_checkout, name='create-order-checkout'),

    # JWT token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User CRUD (admin/self)
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
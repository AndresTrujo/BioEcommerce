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
    payment_sheet,
    confirm_payment_intent,
    stripe_webhook,
)
from rest_framework_simplejwt.views import TokenRefreshView
from .views import EmailTokenObtainPairView

urlpatterns = [
    path('products/', ProductoView.as_view(), name='producto-list'),

    # Auth / users
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/password/reset/', PasswordResetRequestView.as_view(), name='auth-password-reset'),
    path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='auth-password-reset-confirm'),
    path('auth/password/change/', ChangePasswordView.as_view(), name='auth-password-change'),
    path('orders/create-checkout/', create_order_checkout, name='create-order-checkout'),
    path('payment-sheet/', payment_sheet, name='payment-sheet'),
    path('payments/confirm-intent/', confirm_payment_intent, name='confirm-payment-intent'),
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),

    # JWT token endpoints
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User CRUD (admin/self)
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
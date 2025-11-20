from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer
from products.models import Producto
import os
from django.conf import settings
import stripe
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from orders.models import Order_Model, Order_Item

# configure stripe with secret key from settings
stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY', None)

User = get_user_model()
token_generator = PasswordResetTokenGenerator()


# Product list API (existing)
@method_decorator(cache_page(60*5), name='dispatch')
class ProductoView(APIView):
    def get(self, request):
        qs = Producto.objects.select_related('PROD_CATEGORIA').all()
        rows = qs.values('ID_PRODUCTO', 'PROD_NOMBRE', 'PROD_PRECIO_PUB', 'PROD_CATEGORIA__CAT_NOMBRE', 'PROD_IMAGEN', 'STOCK_PROD', 'PROD_DESCRIPCION_DESC')
        output = []
        base = request.build_absolute_uri('/')[:-1]
        for r in rows:
            img = r.get('PROD_IMAGEN')
            if img:
                filename = os.path.basename(img)
                media_prefix = settings.MEDIA_URL.strip('/')
                image_url = f"{base}/{media_prefix}/productos/{filename}"
            else:
                image_url = f"{base}/static/img/placeholder.png"
            output.append({
                'ID_PRODUCTO': r['ID_PRODUCTO'],
                'PROD_NOMBRE': r['PROD_NOMBRE'],
                'PROD_PRECIO_PUB': r['PROD_PRECIO_PUB'],
                'PROD_CATEGORIA': r.get('PROD_CATEGORIA__CAT_NOMBRE'),
                'PROD_IMAGEN': image_url,
                'STOCK_PROD': r['STOCK_PROD'],
                'PROD_DESCRIPCION_DESC': r['PROD_DESCRIPCION_DESC'],
            })
        return Response(output)


# Permissions: admin or object owner
class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.is_staff or obj == request.user)


# Users CRUD (list for admin, retrieve/update/delete for self or admin)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]


# Registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Change password (authenticated user)
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({'old_password': 'Incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({'detail': 'Password updated'})


# Password reset request
class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'detail': 'Email requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return Response({'detail': 'Email enviado si existe'}, status=status.HTTP_200_OK)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        # For mobile apps prefer deep link: myapp://reset?uid=...&token=...
        reset_link = f"{request.build_absolute_uri('/').rstrip('/')}/reset-password?uid={uid}&token={token}"
        subject = 'Restablece tu contraseña'
        # Include UID and token explicitly so the user can paste them in the app
        message = (
            f"Hola,\n\nSe ha solicitado restablecer la contraseña de tu cuenta.\n\n"
            f"Enlace directo: {reset_link}\n\n"
            f"Si el enlace no funciona o prefieres usar la app, usa estos valores: \n"
            f"UID: {uid}\n"
            f"Token: {token}\n\n"
            f"Si no solicitaste este cambio, ignora este correo."
        )
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None)
        try:
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[user.email])
        except Exception as e:
            # don't expose internal errors to caller; log and continue
            try:
                import logging
                logging.getLogger('django').exception('Error sending password reset email: %s', e)
            except Exception:
                pass
        return Response({'detail': 'Email enviado si existe'}, status=status.HTTP_200_OK)


# Password reset confirm
class PasswordResetConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')
        if not all([uid, token, new_password]):
            return Response({'detail': 'Parámetros incompletos'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            pk = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=pk)
        except Exception:
            return Response({'detail': 'Link inválido'}, status=status.HTTP_400_BAD_REQUEST)

        if not token_generator.check_token(user, token):
            return Response({'detail': 'Token inválido o expirado'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'detail': 'Contraseña actualizada'}, status=status.HTTP_200_OK)


# API endpoint for mobile/web clients to create an order and get a Stripe Checkout URL
@api_view(['POST'])
@permission_classes([AllowAny])
def create_order_checkout(request):
    """Accepts JSON with: full_name, email, address, items: [{ productId, quantity }]
    Creates Order_Model + Order_Item entries and a Stripe Checkout session, returns checkout_url.
    """
    import logging, traceback
    from decimal import Decimal
    logger = logging.getLogger('django.request')
    try:
        data = request.data
        # Debug: log request content-type and raw body to help diagnose TypeError
        try:
            raw_body = request.body.decode('utf-8') if request.body else '<empty body>'
        except Exception:
            raw_body = '<unreadable body>'
        logger.error('create_order_checkout called: method=%s, content_type=%s, raw_body=%s', request.method, request.content_type, raw_body)

        items = data.get('items', [])
        full_name = data.get('full_name') or data.get('name') or ''
        email = data.get('email')
        address = data.get('address', '')

        if not isinstance(items, list) or not items:
            return Response({'detail': 'No items provided or invalid items format'}, status=status.HTTP_400_BAD_REQUEST)

        # Create order (associate with user when available)
        order = Order_Model.objects.create(FULL_NAME=full_name or (email.split('@')[0] if email else 'Guest'), EMAIL=email or '', ADDRESS=address, USER=(request.user if getattr(request, 'user', None) and request.user.is_authenticated else None))

        line_items = []
        for it in items:
            pid = it.get('productId')
            qty = int(it.get('quantity', 1) or 1)
            try:
                product = Producto.objects.get(ID_PRODUCTO=pid)
            except Producto.DoesNotExist:
                # rollback created order
                order.delete()
                return Response({'detail': f'Product {pid} not found'}, status=status.HTTP_400_BAD_REQUEST)

            # Ensure price is Decimal
            price_val = getattr(product, 'PROD_PRECIO_PUB', None)
            try:
                price_decimal = Decimal(price_val) if price_val is not None else Decimal('0.00')
            except Exception:
                price_decimal = Decimal('0.00')

            Order_Item.objects.create(ORDER=order, PRODUCT=product, PRICE=price_decimal, QUANTITY=qty)

            unit_amount = int((price_decimal * Decimal(100)).to_integral_value())
            line_items.append({
                'price_data': {
                    'currency': 'mxn',
                    'product_data': {'name': product.PROD_NOMBRE},
                    'unit_amount': unit_amount,
                },
                'quantity': qty,
            })

        # Create Stripe Checkout session
        try:
            host = request.get_host()
            success_url = getattr(settings, 'STRIPE_SUCCESS_URL', None) or f"{request.scheme}://{host}/orders/success/"
            cancel_url = getattr(settings, 'STRIPE_CANCEL_URL', None) or f"{request.scheme}://{host}/orders/cancel/"

            deep_success = getattr(settings, 'MOBILE_DEEP_LINK_SUCCESS', None)
            if deep_success:
                success_url = deep_success

            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
                metadata={'order_id': order.id}
            )
        except Exception as e:
            order.delete()
            logger.exception('Error creating Stripe session')
            return Response({'detail': 'Error creating Stripe session', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'checkout_url': getattr(checkout_session, 'url', None) or checkout_session.get('url') if isinstance(checkout_session, dict) else None, 'order_id': order.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        tb = traceback.format_exc()
        logger.error('Exception in create_order_checkout: %s\n%s', str(e), tb)
        detail = {'detail': 'Server error creating order', 'error': str(e)}
        if settings.DEBUG:
            detail['traceback'] = tb
        return Response(detail, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
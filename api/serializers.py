from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from products.models import Producto, Categoria

User = get_user_model()


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['ID_PRODUCTO', 'PROD_NOMBRE', 'PROD_PRECIO_PUB', 'PROD_IMAGEN', 'PROD_DISPONIBLE', 'PROD_GRAMAJE', 'PROD_CATEGORIA']
        read_only_fields = ['ID_PRODUCTO']
        

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['CAT_NOMBRE', 'CAT_SLUG']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError({"email": "Este email ya está registrado."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)
        password = validated_data.pop('password')
        # create_user handles password hashing
        user = User.objects.create_user(password=password, **validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

        
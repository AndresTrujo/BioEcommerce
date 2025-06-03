# users/models.py

from django.db import models
# Importa para obtener el modelo de usuario
from django.contrib.auth import get_user_model
# Para crear el perfil automáticamente
from django.db.models.signals import post_save
from django.dispatch import receiver  # Para el decorador del signal

# Obtén el modelo de usuario activo de Django (el default en este caso)
User = get_user_model()


class UserProfile(models.Model):
    # Relación uno a uno con el modelo User de Django
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    # Campos adicionales que quieres guardar para el usuario
    sexo = models.CharField(
        max_length=20,
        choices=[
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
            ('no-especificar', 'Prefiero no especificar')
        ],
        blank=True,  # Permite que el campo esté vacío
        null=True    # Permite valores NULL en la base de datos
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)

    # Puedes añadir un campo de dirección aquí si no lo tienes en el modelo Order
    # y quieres que el perfil del usuario lo guarde.
    # address = models.CharField(max_length=250, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    # postal_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Signal para crear automáticamente un UserProfile cuando se crea un User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

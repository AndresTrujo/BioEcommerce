from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    sexo = models.CharField(
        max_length=20,
        choices=[
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
            ('no-especificar', 'Prefiero no especificar')
        ],
        blank=True,
        null=True
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Signal para crear automáticamente un UserProfile cuando se crea un User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Crea un UserProfile para cada nuevo usuario que se registra.
    """
    if created:
        UserProfile.objects.create(user=instance)

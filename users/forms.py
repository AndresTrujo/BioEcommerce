from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile # Importa tu nuevo modelo de perfil

# Importa el modelo User de Django para acceder a sus campos
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterForm(UserCreationForm):
    # Campos del modelo User por defecto que quieres en el formulario
    # first_name y last_name ya están en el modelo User por defecto
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True) # El campo email en UserCreationForm es opcional, lo hacemos requerido

    # Campos del UserProfile
    sexo = forms.ChoiceField(
        choices=[
            ('', 'Selecciona tu sexo'), # Opción por defecto
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
            ('no-especificar', 'Prefiero no especificar')
        ],
        required=True # O False si quieres que sea opcional
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), # Widget HTML5 para fecha
        required=True # O False si quieres que sea opcional
    )

    class Meta(UserCreationForm.Meta):
        model = User # Apunta al modelo User por defecto de Django
        # Incluye los campos de UserCreationForm y los que queremos del modelo User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

    # Sobrescribe el método save para guardar tanto el User como el UserProfile
    def save(self, commit=True):
        # Primero, guarda el usuario (username, password, password2, email, first_name, last_name)
        user = super().save(commit=False) # No lo guardes aún en la DB
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email'] # Asegura que el email se guarda en el User
        if commit:
            user.save() # Guarda el User en la DB

        # Ahora, crea y guarda el UserProfile asociado
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.sexo = self.cleaned_data['sexo']
        profile.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if commit:
            profile.save() # Guarda el UserProfile en la DB

        return user # Devuelve el objeto User
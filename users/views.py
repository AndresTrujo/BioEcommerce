from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegisterForm # ¡Importa tu formulario personalizado!

class SignUpView(generic.CreateView):
    form_class = UserRegisterForm # ¡CAMBIO AQUÍ! Usa tu formulario personalizado
    success_url = reverse_lazy('login') # Redirige al login después del registro exitoso
    template_name = 'registration/signup.html'

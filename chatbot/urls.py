from django.urls import path
from .views import chatbot_view

urlpatterns = [
    path('api/', chatbot_view, name='chatbot_api'),
]

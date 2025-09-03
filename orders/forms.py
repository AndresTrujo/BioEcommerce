from django import forms
from .models import Order_Model


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order_Model
        fields = ['FULL_NAME', 'EMAIL', 'ADDRESS']
        widgets = {
            'FULL_NAME': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-700 text-[#1E1E1E]'
            }),
            'EMAIL': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-700 text-[#1E1E1E]'
            }),
            'ADDRESS': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-700 text-[#1E1E1E]'
            }),
        }

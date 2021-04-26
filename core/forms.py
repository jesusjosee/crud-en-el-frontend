from .models import Product
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'manufacturing': forms.SelectDateWidget()
        }

class CustomUserCreationFrom(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
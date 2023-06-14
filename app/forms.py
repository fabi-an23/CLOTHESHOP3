from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactoForms(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class CustomUserCreationForms(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
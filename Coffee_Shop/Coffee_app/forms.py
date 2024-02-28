# forms.py

from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    telefono = forms.CharField(max_length=10, required=True)

class AsociadoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    puesto = forms.CharField(max_length=100, required=True)
    calificacion = forms.IntegerField(required=True)

class BebidaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=8, decimal_places=2, required=True)
    
class PostreForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=8, decimal_places=2, required=True)

class MerchForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=8, decimal_places=2, required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Agregar 'password' al formulario

class AvatarForm(forms.Form):
    foto = forms.ImageField(required=True)


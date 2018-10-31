from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perritos

from .models import Perfil

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perritos
        fields = ['nombre','raza','desc', 'estado', 'imagen']
        labels = {'nombre':'Nombre','raza':'Raza','estado':'Estado', 
        'desc':'Descripcion', 'imagen':'Imagen'}

from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'status',]



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'status', ]

"""from django.forms import ModelForm
from .models import UsuarioDisciplina

class ResevarDiscForm(ModelForm):
    class Meta:
        model = UsuarioDisciplina
        fields = '__all__'
        exclude = ('status')"""

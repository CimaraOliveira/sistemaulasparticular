from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from disciplina.models import UsuarioDisciplina, Usuario

class ReservarDiscForm(ModelForm):
    class Meta:
        model = UsuarioDisciplina
        fields = '__all__'


class AlterDadoUsuForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'






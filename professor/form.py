from django import forms
from django.forms import ModelForm
from .models import Disciplina, Professor, UsuarioDisciplina

class CadDiscForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        exclude = ('slug',)

class CadProfForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class ReservarDiscForm(ModelForm):
    class Meta:
        model = UsuarioDisciplina
        fields = '__all__'



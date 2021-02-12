from django import forms
from django.forms import ModelForm
from .models import Disciplina

class CadDiscForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

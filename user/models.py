from django.contrib.auth.models import User
from django.db import models
from disciplina.models import UsuarioDisciplina,  Usuario
from django import forms

class FormUsuDisc(forms.ModelForm):
    class Meta:
        model = UsuarioDisciplina
        exclude = ()


class FormDadosUsu(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('usuario','is_active','slug','aluno','professor',)


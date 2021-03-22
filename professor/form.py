from django import forms
from django.forms import ModelForm
from disciplina.models import Disciplina, Professor, UsuarioDisciplina

class CadDiscForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        exclude = ('slug','usuario','professor',)

class CadProfForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'descricao_curta', 'descricao_longa', 'imagem','slug',]
        exclude = ('usuario',)

class ReservarDiscForm(ModelForm):
    class Meta:
        model = UsuarioDisciplina
        fields = '__all__'
        exclude = ()



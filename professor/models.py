from disciplina.models import Disciplina, Professor, UsuarioDisciplina
from django import forms

class FormDisciplina(forms.ModelForm):
    class Meta:
        model = Disciplina
        exclude = ('slug',)

class FormProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        exclude =('slug','professor',)

class FormUsuDisc(forms.ModelForm):
    class Meta:
        model = UsuarioDisciplina
        exclude = ('usuario','disciplina',)





from disciplina.models import UsuarioDisciplina, Usuario, Disciplina
from django import forms

class FormUsuDisc(forms.ModelForm):
    class Meta:
        model = UsuarioDisciplina
        exclude = ()


class FormDadosUsu(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('is_active','slug','is_staff','is_superuser','telefone','user_permissions','groups','last_login','password','status',)

class FormCreateUsu(forms.ModelForm):
    models = Usuario
    exclude = ('is_active', 'slug',)

class FormDisciplina(forms.ModelForm):
    class Meta:
        model = Disciplina
        exclude = ('slug',)



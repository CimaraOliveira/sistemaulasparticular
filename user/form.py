from django.forms import ModelForm
from disciplina.models import UsuarioDisciplina, Usuario

class ReservarDiscForm(ModelForm):
    class Meta:
        model = UsuarioDisciplina
        fields = '__all__'


class AlterDadoUsuForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'email',]

class UserCreateForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'email', 'password']








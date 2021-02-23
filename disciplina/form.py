from django.forms import ModelForm
from .models import UsuarioDisciplina
class ResevarDiscForm(ModelForm):
    class Meta:
        model = UsuarioDisciplina
        fields = '__all__'
        exclude = ('usuario','status')

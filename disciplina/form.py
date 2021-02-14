from django.forms import ModelForm
from .models import Reserva

class ResevarDiscForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        #exclude = ('slug',)
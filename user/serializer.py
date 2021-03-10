from rest_framework import serializers
from .models import  Usuario, UsuarioDisciplina

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class  UsuarioDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDisciplina
        fields = ('__all__')

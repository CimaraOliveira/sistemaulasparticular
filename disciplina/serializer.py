from rest_framework import serializers
from .models import Disciplina, Usuario

class DiscipilnaApi(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields  = '__all__'


class UsuarioApi(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
from rest_framework import serializers
from .models import Disciplina


class DiscipilnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ('__all__')






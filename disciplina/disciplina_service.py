from rest_framework import viewsets
from .models import Disciplina
from disciplina.serializer import DiscipilnaSerializer


class listarDisciplina(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DiscipilnaSerializer






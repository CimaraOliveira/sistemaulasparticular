from rest_framework import viewsets
from disciplina.models import Professor
from professor.serializer import ProfessorSerializer

class listarProfesor(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
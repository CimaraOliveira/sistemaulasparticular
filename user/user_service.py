from rest_framework import viewsets
from disciplina.models import Usuario, UsuarioDisciplina
from user.serializer import UsuarioSerializer, UsuarioDisciplinaSerializer


class listarUsuario(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class listarReservasUsuario(viewsets.ModelViewSet):
    queryset = UsuarioDisciplina.objects.all()
    serializer_class = UsuarioDisciplinaSerializer
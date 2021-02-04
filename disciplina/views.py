from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

class Home(ListView):
    model = models.Disciplina
    template_name = 'disciplina/home.html'
    context_object_name = 'disciplinas'

class Disciplina(ListView):
    model = models.Disciplina
    template_name = 'disciplina/disciplina.html'
    context_object_name = 'disciplinas'


def professor(request):
    return render(request, 'disciplina/professor.html')

def listarDisciplinas(request):
    return render(request, 'disciplina/listarDisciplinas.html')

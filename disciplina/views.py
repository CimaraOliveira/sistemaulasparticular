from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models

class Home(ListView):
    model = models.Disciplina
    template_name = 'disciplina/home.html'
    context_object_name = 'disciplinas'

class DetalhesDisciplina(DetailView):
    model = models.Disciplina
    template_name = 'disciplina/detalhesDisciplina.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'


"""class Disciplina(ListView):
    model = models.Disciplina
    template_name = 'disciplina/disciplina.html'
    context_object_name = 'disciplinas'"""


def professor(request):
    return render(request, 'disciplina/professor.html')


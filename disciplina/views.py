from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
#from .models import FormReserva
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required



from .models import Disciplina
from django.contrib.auth import authenticate, login
import copy

from . import models

"""class Home(ListView):
    model = models.Disciplina
    template_name = 'disciplina/home.html'

    context_object_name = 'disciplinas'"""

class DetalhesDisciplina(DetailView):
    model = models.Disciplina
    template_name = 'disciplina/detail.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'

def professor(request):
    return render(request, 'disciplina/professor.html')

#@login_required(redirect_field_name='login')
def listar(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplina/listar.html', context)



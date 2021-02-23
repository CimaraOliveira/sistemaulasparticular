from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib import messages, auth
from django.shortcuts import render, redirect, reverse


from .models import Disciplina,UsuarioDisciplina
import copy
from .functions import getNrDisciplina
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin



"""class Home(ListView):
    model = models.Disciplina
    template_name = 'disciplina/home.html'

    context_object_name = 'disciplinas'"""

class DetalhesDisciplina(DetailView):
    model = models.Disciplina
    template_name = 'disciplina/detalhesDisciplina.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'

@login_required()
def professor(request):
    return render(request, 'disciplina/professor.html')

#@login_required()
def listar(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplina/listar.html', context)

def home(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplina/home.html', context)

#@login_required(login_url='user:login')
def reservarDisciplina(request, slug):
    """if not request.user.is_authenticated():
        return redirect('user:login')"""
    disciplina = get_object_or_404(Disciplina, slug = slug)
    usuarioDisciplina, created = UsuarioDisciplina.objects.get_or_create(usuario=request.user,disciplina=disciplina)

    if created:
         usuarioDisciplina.active()
         messages.info(request, 'Você já está inscrito nessa Disciplina!')

    messages.success(request, 'Sua solicitação vai ser analisada!')
    return redirect('disciplina:listar')



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib import messages, auth
from django.shortcuts import render, redirect, reverse
from django.core.validators import validate_email
from . import models
from django.db.models.functions import Concat
from .models import Usuario, Disciplina, UsuarioDisciplina,Professor
from django.core.paginator import Paginator
from django.db.models import Q, Value


def criar(request):
    if request.method != 'POST':
        return render(request, 'disciplina/criar.html')

    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    status = request.POST['status']
    password = request.POST['password']
    password1 = request.POST['password1']

    messages.success(request, 'Usuário Registrado com Sucesso!')

    new_user = Usuario.objects.create_superuser(username=username, first_name=first_name, last_name=last_name,
                         email=email,  status=status, password=password)
    new_user.save()
    return redirect('user:user_login')



class DetalhesDisciplina(DetailView):
    model = models.Disciplina
    template_name = 'disciplina/detalhesDisciplina.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'


#@csrf_exempt
@login_required(login_url='user:user_login')
def listar(request):
    disciplinas = Disciplina.objects.all()
    paginator = Paginator(disciplinas, 6)
    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)

    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplina/listar.html', context)


@login_required(login_url='user:user_login')
def reservarDisciplina(request, slug):
    disciplina = get_object_or_404(Disciplina, slug=slug)
    usuarioDisciplina, created = UsuarioDisciplina.objects.get_or_create(usuario=request.user, disciplina=disciplina)

    """if created:
         usuarioDisciplina.active()
         messages.info(request, 'Você já está inscrito nessa Disciplina!')"""

    messages.success(request, 'Sua solicitação vai ser analisada!')
    return redirect('disciplina:listar')

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.error(request, 'Campo não pode ser vazio!')
        return redirect('disciplina:listar')


    campos = Concat('nome', Value(' '), 'titulo')

    disciplinas = Disciplina.objects.annotate(
        nome_disciplina=campos
    ).filter(
        Q(nome_disciplina__icontains=termo)
    )

    if not disciplinas:
        messages.error(request, 'Disciplina não existe!')
        return redirect('disciplina:listar')

    paginator = Paginator(disciplinas, 6)
    page = request.GET.get('p')
    disciplinas = paginator.get_page(page)

    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplina/busca.html', context)


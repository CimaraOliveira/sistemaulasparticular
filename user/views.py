from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from disciplina.models import Disciplina,Usuario
from .models import FormUsuDisc,  FormDadosUsu


#@login_required(redirect_field_name='login')
class HomeUsuario(ListView):
    model = Disciplina
    template_name = 'disciplina/home.html'

    context_object_name = 'disciplinas'


class DetalhesDisciplina(DetailView):
    model = Disciplina
    template_name = 'user/detail.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'


def criar(request):
    if request.method != 'POST':
        return render(request, 'user/criar.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not email or not usuario or not senha \
            or not senha2:
        messages.error(request, 'Preencha todos os Campos!')
        return render(request, 'user/criar.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Inválido!')
        return render(request, 'user/criar.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter pelo menos 6 Caracteres!')
        return render(request, 'user/criar.html')

    if senha != senha2:
        messages.error(request, 'Senhas não Conferem!')
        return render(request, 'user/criar.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'user/criar.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Esse nome de Usuário já existe!')
        return render(request, 'user/criar.html')

    messages.success(request, 'Usuário Registrado com Sucesso!')

    user = User.objects.create_user(email=email, username=usuario, password=senha,
                                    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('user:login')


def login(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')

    if request.method != 'POST':
        return render(request, 'user/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')

    user = auth.authenticate(request, username=usuario, password=senha)

    if user is not None:
        if user.is_active:
           messages.success(request, 'Login efetuado com Sucesso!')
           return redirect('disciplina:listar')

    messages.error(request, 'Usuário ou Senha Inválidos!')
    return redirect('user:login')


def index(request):
    pass
    #return redirect(request,'user:login')"""

def reservarDisciplina(request):
    form = FormUsuDisc(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('user:reservarDisciplina')
    else:
        form = FormUsuDisc(request.POST, request.FILES)

    context = {
        'form': form
    }

    return render(request, 'user/reservarDisciplina.html', context)

def editarUsuario(request):
    data = {}
    usuario = Usuario.objects.get(id=id)
    form = FormDadosUsu(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('user:editarUsuario')

    data['form'] = form
    data['disciplina'] = usuario

    return render(request, 'user/editarUsuario.html', data)




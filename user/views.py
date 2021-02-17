from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from disciplina.models import Disciplina,Usuario, UsuarioDisciplina
from django.http import HttpResponseRedirect

from django.views import View

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


"""def criar(request):
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
    #return redirect('login')"""


def criar(request):
    if request.method != 'POST':
        return render(request, 'user/criar.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    user_choice = request.POST.get('user_choice')

    if not nome or not email or not usuario or not senha \
            or not user_choice or not senha2:
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

    user = User.objects.create_user(email=email, username=usuario,  password=senha,
                                    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('user:login')
    #return redirect('login')

def login(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')
        #return redirect('login')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')
        #return redirect('login')

    if request.method != 'POST':
        return render(request, 'user/login.html')
        #return redirect('login')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')

        #return redirect('login')

    user = auth.authenticate(request, username=usuario, password=senha)

    if user is not None:
        if user.is_active:
                messages.success(request, 'Login efetuado com Sucesso!')
                return redirect('disciplina:listar')





    messages.error(request, 'Usuário ou Senha Inválidos!')
    return redirect('user:login')
    #return redirect('login')

"""def login(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')
        #return redirect('login')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')
        #return redirect('login')

    if request.method != 'POST':
        return render(request, 'user/login.html')
        #return redirect('login')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')

        #return redirect('login')

    user = auth.authenticate(request, username=usuario, password=senha)

    if user is not None:
        if user.is_active:
           messages.success(request, 'Login efetuado com Sucesso!')
           return redirect('disciplina:listar')

    messages.error(request, 'Usuário ou Senha Inválidos!')
    return redirect('user:login')
    #return redirect('login')
"""

def index(request):
    return render(request,'user/index.html')

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

    if request.user.is_authenticated:
       id = request.user
       usuario = Usuario.objects.all()
       profile = Usuario.objects.get(usuario=usuario)

    else:
        usuario = ""
        profile = ""

    context = {
            'usuario' :"usuario",
            'profile' : "profile"
        }

    return render(request, 'user/editarUsuario.html', context)

def detalhesUsuario(request):
    user = Usuario.objects.all()
    context = {
        'user': user
    }
    return render(request, 'user/detalhesUsuario.html', context)

#@login_required()
def user_logout(request):
    logout(request)
    return redirect('user:login')

def alterarSenha(request):
    pass

def minhasDisciplinas(request):
    username = request.user.username
    disciplinas = Usuario.objects.filter(id=id)
    context ={
        'disciplinas' : disciplinas
    }
    return render(request, 'user/minhasDisciplinas.html', context)



from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from disciplina.models import Disciplina

from django.contrib.auth.decorators import login_required

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

    messages.success(request, 'Usuário Registrado com Sucesso!')

    user = User.objects.create_user(email=email, username=usuario, password=senha,
                                    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')

def login(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')

    email = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, email=email, password=senha)

    if not user:
        messages.error(request, 'Usuário ou Senha Inválidos!')
        return render(request, 'user/login.html')

    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com Sucesso!')
        return redirect('home')



#@login_required(redirect_field_name='login')
class HomeUsuario(ListView):
    model = Disciplina
    template_name = 'disciplina/home.html'

    context_object_name = 'disciplinas'


def logout(request):
    auth.logout(request)
    return redirect('login')



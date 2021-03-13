from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import FormDadosUsu
from disciplina.models import UsuarioDisciplina, Usuario
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordChangeView,PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def user_login(request):
    if request.method != 'POST':
        return render(request, 'user/user_login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:user_login')

    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
        if user.status == 'aluno' or user.status == 'professor':
            login(request, user)
            if user.status == 'aluno':
               return redirect('disciplina:listar')
            if user.status == 'professor':
                return redirect('disciplina:listar')

    messages.error(request, 'Usuário ou Senha Inválidos!')
    return redirect('user:user_login')


@login_required(login_url='user:user_login')
def minhasDisciplinas(request):
    usuariodisciplinas = UsuarioDisciplina.objects.filter(usuario_id = request.user.id)
    context ={
        'usuariodisciplinas' : usuariodisciplinas
    }
    print(usuariodisciplinas)
    return render(request, 'user/minhasDisciplinas.html', context)


@login_required(login_url='user:user_login')
def editarUsuario(request,id):
      data = {}
      usuario = Usuario.objects.get(id=id)
      form = FormDadosUsu(request.POST or None, instance=usuario)

      if form.is_valid():
        form.save()
        messages.success(request, 'Dados alterados com Sucesso!')
        return redirect('disciplina:listar')

      data['form'] = form
      data['usuario'] = usuario
      return render(request, 'user/editarUsuario.html', data)

@login_required(login_url='user:user_login')
def detalhes(request,id):
      data = {}
      usuario = Usuario.objects.get(id=id)
      form = FormDadosUsu(request.POST or None, instance=usuario)

      if form.is_valid():
        form.save()
        return redirect('disciplina:listar')

      data['form'] = form
      data['usuario'] = usuario
      return render(request, 'user/detalhes.html', data)


#@login_required()
def user_logout(request):
    logout(request)
    return redirect('user:user_login')









from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import FormDadosUsu
from disciplina.models import UsuarioDisciplina, Usuario
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordChangeView,PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


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



"""
class DetalhesDisciplina(DetailView):
    model = Disciplina
    template_name = 'user/detail.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'

"""
@login_required(login_url='user:user_login')
def editarUsuario(request,id):
      data = {}
      usuario = Usuario.objects.get(id=id)
      form = FormDadosUsu(request.POST or None, instance=usuario)

      if form.is_valid():
        form.save()
        return redirect('user:editarUsuario')

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

class PasswordReset(SuccessMessageMixin, PasswordResetView):
        template_name = "user/password-reset.html"


class PasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'user/reset_password_sent.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'


class PasswordResetCompleteView(SuccessMessageMixin, PasswordResetCompleteView):
    success_message = 'Senha Alterada com sucesso!'
    template_name = 'user/user_login.html'


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/password-change.html'
    success_url = '/disciplina/listar'
    #success_message = "Senha alterada com sucesso!


"""def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'user/change_password.html', {
            'form': form
        })"""

from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,\
    PasswordChangeView,PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin

"""class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = "registration/password-reset-form.html"""


"""class PasswordResetDone(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'accounts/reset_password_sent.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

class PasswordResetCompleteViews(SuccessMessageMixin,PasswordResetCompleteView):
    success_message = 'Senha Alterada com Sucesso!'
    template_name = 'user/login.html'

class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = '/disciplina/listar'
    success_message = "Sua senha foi alterada com sucesso!"""
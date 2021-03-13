from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [

   path('password-reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password-reset.html"), name='password-reset'),
   path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password-reset-done.html"),
        name='password-reset-done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_comfirm'),
   path('reset_password_complete/', auth_views.PasswordChangeView.as_view(template_name="accounts/reset_password_complete.html"), name='password_reset_complete'),


]
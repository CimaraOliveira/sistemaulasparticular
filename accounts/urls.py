from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

   path('password-reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password-reset.html"), name='password-reset'),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"),  name='reset_password_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_comfirm'),
   #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_confirm'),
   path('reset_password-complete/', auth_views.PasswordChangeView.as_view(template_name="accounts/reset_password-complete.html"), name='password_reset_done'),


]
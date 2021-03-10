from django.urls import path,include
from . import views
from .views import PasswordReset,PasswordResetDone,PasswordResetCompleteView,PasswordResetConfirm, PasswordChange
from django.contrib.auth.views import PasswordResetDoneView



urlpatterns = [

   path('password-reset/', PasswordReset.as_view(), name='password-reset'),
   path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_complete'),
   path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   path('password-change/', PasswordChange.as_view(), name='password-change'),
   path('', include('django.contrib.auth.urls')),

]
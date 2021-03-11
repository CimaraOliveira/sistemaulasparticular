from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views


app_name = 'user'

urlpatterns = [

   path('user_login/', views.user_login, name='user_login'),
   path('logout/', views.user_logout, name='user_logout'),
   path('minhasDisciplinas/', views.minhasDisciplinas, name='minhasDisciplinas'),
   path('editarUsuario/<int:id>', views.editarUsuario, name='editarUsuario'),
   path('detalhes/<int:id>', views.detalhes, name='detalhes'),

   #path('password/', views.change_password, name='change_password'),




]
from django.urls import path
from . import views

#app_name = 'user'

urlpatterns = [

   path('criar/', views.criar, name='criar'),
   path('login/', views.login, name='login'),
   #path('logout/', views.logout, name='logout'),
   #path('homeusuario/', views.logout, name='homeusuario'),
   path('homeusuario/', views.HomeUsuario.as_view(), name='homeusuario'),





]
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [

   path('criar/', views.criar, name='criar'),
   #path('criar/', views.Criar.as_view(), name='criar'),
   path('login/', views.login, name='login'),
   path('logout/', views.user_logout, name='user_logout'),
   #path('index/', views.index, name='index'),
   #path('homeusuario/', views.logout, name='homeusuario'),
   path('homeusuario/', views.HomeUsuario.as_view(), name='homeusuario'),
   #path('<slug>', views.DetalhesDisciplina.as_view(), name='detalhesDisciplina'),

]
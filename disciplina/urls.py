from django.urls import path
from . import views

#app_name = 'disciplina'

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('<slug>', views.DetalhesDisciplina.as_view(), name='detalhesDisciplina'),
    #path('', views.Disciplina.as_view(), name='listar'), #primeira pagina login

    path('professor/', views.professor, name='professor'),
    #path('professor/', views.professor, name='professor'),
    #path('<int:contato_id>', views.ver_contato, name='ver_contato'),


]
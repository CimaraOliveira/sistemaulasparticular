from django.urls import path
from . import views

app_name = 'disciplina'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('<slug>', views.DetalhesDisciplina.as_view(), name='detalhesDisciplina'),
    #path('reservarDisciplina/', views.reservarDisciplina, name='reservarDisciplina'),
     # path('reservarDisciplina/<slug:slug>/', views.reservarDisciplina, name='reservarDisciplina'),
    #path('reservarDisciplina/', views.ReservarDisciplina.as_view(), name='reservarDisciplina'),


]
from django.urls import path
from . import views

app_name = 'disciplina'

urlpatterns = [
    path('criar/', views.criar, name='criar'),
    path('', views.listar, name='listar'),
    path('<slug>', views.DetalhesDisciplina.as_view(), name='detalhesDisciplina'),
    path('reservarDisciplina/<slug:slug>/', views.reservarDisciplina, name='reservarDisciplina'),



]
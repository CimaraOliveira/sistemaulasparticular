from django.urls import path
from . import views

app_name = 'disciplina'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('<slug>', views.DetalhesDisciplina.as_view(), name='detalhesDisciplina'),





]
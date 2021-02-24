from django.urls import path
from . import views

app_name = 'professor'

urlpatterns = [
   path('cadastrarDisc/', views.cadastrarDisc, name='cadastrarDisc'),
   path('detail/', views.detail, name='detail'),
   path('editarDisciplina/<int:id>', views.editarDisciplina, name='editarDisciplina'),
   path('removerDisciplina/<int:id>', views.removerDisciplina, name='removerDisciplina'),
   path('cadastroProfessor/', views.cadastroProfessor, name='cadastroProfessor'),
   path('detalhesProfessor/', views.detalhesProfessor, name='detalhesProfessor'),
   path('editarProfessor/<int:id>', views.editarProfessor, name='editarProfessor'),
   path('listarPedidosReserva/', views.listarPedidosReserva, name='listarPedidosReserva'),
   path('alterarStatusReserva/<int:id>', views.alterarStatusReserva, name='alterarStatusReserva'),










]


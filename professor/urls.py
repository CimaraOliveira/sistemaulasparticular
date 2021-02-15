from django.urls import path
from . import views

app_name = 'professor'

urlpatterns = [
   #path('cadastroDisciplina/', views.cadastroDisciplina, name='cadastroDisciplina'),
   path('cadastrarDisc/', views.cadastrarDisc, name='cadastrarDisc'),
   path('detail/', views.detail, name='detail'),
   path('editarDisciplina/<int:id>', views.editarDisciplina, name='editarDisciplina'),
   path('removerDisciplina/<int:id>', views.removerDisciplina, name='removerDisciplina'),

   #path('cadastrarDisc/', views.CadastrarDisc.as_view(), name='cadastrarDisc'),
   #path('cadastrarDisc/', views.CadastrarDisc.as_view(), name='cadastrarDisc'),

]


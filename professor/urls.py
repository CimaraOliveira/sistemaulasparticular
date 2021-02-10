from django.urls import path
from . import views

app_name = 'professor'

urlpatterns = [
   path('cadastroDisciplina/', views.cadastroDisciplina, name='cadastroDisciplina'),
]
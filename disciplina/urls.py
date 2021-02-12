from django.urls import path
from . import views

app_name = 'disciplina'

urlpatterns = [
    #path('home/', views.home, name='home'),

    path('', views.Home.as_view(), name='home'),
    path('<slug>', views.DetalhesDisciplina.as_view(), name='detalhesDisciplina'),
    path('prof/', views.professor, name='prof'),




]
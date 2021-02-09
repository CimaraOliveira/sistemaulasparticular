from django.urls import path
from . import views

#app_name = 'disciplina'

urlpatterns = [
    #path('home/', views.home, name='home'),

    path('', views.Home.as_view(), name='home'),


    path('professor/', views.professor, name='professor'),




]
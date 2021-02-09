from django.urls import path
from . import views

#app_name = 'user'

urlpatterns = [

   path('criar/', views.criar, name='criar'),
   path('login/', views.login, name='login'),




]
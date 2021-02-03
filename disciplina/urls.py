from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('professor/', views.professor, name='professor'),
    #path('<int:contato_id>', views.ver_contato, name='ver_contato'),


]
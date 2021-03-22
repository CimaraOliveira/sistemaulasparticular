from django.urls import path
from .views import GeneratePdf


urlpatterns = [
    path('relatorios/', GeneratePdf.as_view(), name='gerar_relatorio'),

]
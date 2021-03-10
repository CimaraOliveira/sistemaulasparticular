from django.urls import path, include
from .views import GeneratePdf,write_pdf_view, GeneratePDF

urlpatterns = [
    path('relatorios/', GeneratePdf.as_view(), name='gerar_relatorio'),

]
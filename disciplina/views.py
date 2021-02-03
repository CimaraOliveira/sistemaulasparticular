from django.shortcuts import render

def home(request):
    return render(request, 'disciplina/home.html')

def professor(request):
    return render(request, 'disciplina/professor.html')


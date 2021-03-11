from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib import messages, auth
from .models import FormDisciplina, FormProfessor,FormUsuDisc
from disciplina.models import Disciplina,Professor, UsuarioDisciplina,Usuario
from django.contrib.auth.decorators import login_required


@login_required(login_url='user:user_login')
def cadastrarDisc(request):
    form = FormDisciplina(request.POST, request.FILES)

    if form.is_valid():

        form.save()
        return redirect('professor:disProfessor')
    else:
        form = FormDisciplina(request.POST, request.FILES)

    context = {
        'form': form
    }
    return render(request, 'professor/cadastrarDisc.html', context)

@login_required(login_url='user:user_login')
def cadastroProfessor(request):
    form = FormProfessor(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('professor:detalhesProfessor')
        #return redirect('professor:detalhesProfessor')
    else:
        form = FormProfessor(request.POST, request.FILES)

    context = {
        'form': form
    }
    return render(request, 'professor/cadastroProfessor.html', context)

@login_required(login_url='user:user_login')
def detail(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas
    }
    return render(request, 'professor/detail.html', context)

@login_required(login_url='user:user_login')
def editarDisciplina(request,id):
    data = {}
    disciplina = Disciplina.objects.get(id=id)
    form = FormDisciplina(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        return redirect('professor:detail')

    data['form'] = form
    data['disciplina'] = disciplina

    return render(request, 'professor/editarDisciplina.html',data)

@login_required(login_url='user:user_login')
def removerDisciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    disciplina.delete()
    return redirect('professor:detail')

"""@login_required(login_url='user:user_login')
def detalhesProfessor(request):
    professores = Professor.objects.all()
    context = {
        'professores': professores
    }
    return render(request, 'professor/detalhesProfessor.html', context)
"""

@login_required(login_url='user:user_login')
def detalhesProfessor(request):
    professores = Professor.objects.filter(id=request.user.id)
    context = {
        'professores': professores
    }
    return render(request, 'professor/detalhesProfessor.html', context)


@login_required(login_url='user:user_login')
def editarProfessor(request,id):
    data = {}
    professor = Professor.objects.get(id=id)
    form = FormProfessor(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('professor:detalhesProfessor')

    data['form'] = form
    data['professor'] = professor

    return render(request, 'professor/editarProfessor.html',data)

@login_required(login_url='user:user_login')
def listarPedidosReserva(request):
    #usuariodisciplinas = UsuarioDisciplina.objects.filter(disciplina_id=request.user.id)
    usuariodisciplinas = UsuarioDisciplina.objects.filter(disciplina_id= request.user.id)
    context = {
       'usuariodisciplinas': usuariodisciplinas
    }
    return render(request, 'professor/listarPedidosReserva.html', context)

@login_required(login_url='user:user_login')
def alterarStatusReserva(request,id):
    data = {}
    usuariodisciplina = UsuarioDisciplina.objects.order_by('id').get(id=id)
    form = FormUsuDisc(request.POST or None, instance=usuariodisciplina)

    if form.is_valid():
        form.save()
        return redirect('professor:listarPedidosReserva')

    data['form'] = form
    data['usuariodisciplina'] = usuariodisciplina

    return render(request, 'professor/alterarStatusReserva.html', data)

@login_required(login_url='user:user_login')
def disProfessor(request):
    professor = request.user
    #professor1 = Professor.objects.get(nome=usuario.username)
    #professoeDisciplinas = Disciplina.objects.filter(professor_id=request.user.id)
    professoeDisciplinas = Disciplina.objects.filter(professor=professor.id)
    context = {
        'professoeDisciplinas': professoeDisciplinas
    }
    return render(request, 'professor/disProfessor.html', context)






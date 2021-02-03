from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/',blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Disciplina(models.Model):
    usuario = models.ManyToManyField(Usuario)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    titulo = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/',
                               blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome or self.professor
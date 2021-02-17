from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, UserManager
import os
from PIL import Image
from django.utils.text import slugify

from django.db.models import Q
from django.urls import reverse
from django import forms

from django.utils import timezone


class Professor(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    # disciplina = models.ForeignKey(Disciplina)
    usuario = models.CharField('User', max_length=30)
    is_active = models.BooleanField('Ativo', default=False)
    slug = models.SlugField('Atalho', max_length=200, null=True, blank=True)
    nome = models.CharField('Nome', max_length=30)
    sobrenome = models.CharField('Sobrenome', max_length=30, blank=True)
    email = models.CharField('E-mail', max_length=30, blank=True)
    telefone = models.CharField('Telefone', max_length=20)

    USER_CHOICES = (
        ("m", "Adm"),
        ("p", "Professor"),
        ("a", "Aluno")
    )
    user_choice = models.CharField(max_length=1, choices=USER_CHOICES, blank=False, null=False)


class Meta:
      verbose_name = ('Usuário')
      verbose_name_plural = ('Usuários')


def save(self, *args, **kwargs):
    if not self.slug:
        slug = f'{slugify(self.nome)}'
        self.slug = slug

    super().save(*args, **kwargs)

    def get_id(self):
        return self.id


class Disciplina(models.Model):
    # usuarios = models.ManyToManyField(Usuario)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=50)
    titulo = models.TextField('Título', max_length=25)
    descricao_longa = models.TextField('Descrição')
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField('Atalho', unique=True, blank=True, null=True)
    data_inicio = models.DateField('Data Início', null=True, blank=True)

    # data_reserva = models.DateTimeField('Data Início',default=timezone.now)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size

        if (original_width <= new_width):
            img_pill.close()
            return

        new_height = round((new_width * original_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        def save(self, *args, **kwargs):
            if not self.id:
                id = f'{slugify(self.nome)}'
                self.slug = id

            super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome or self.professor


class UsuarioDisciplina(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="linguagem")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name="linguagem")
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    data_reserva = models.DateField('Data Reserva', null=True, blank=True)

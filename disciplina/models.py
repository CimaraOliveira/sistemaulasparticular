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
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/',blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome



class Usuario(models.Model):
   #disciplina = models.ForeignKey(Disciplina)
    is_active = models.BooleanField('Ativo', default=False)
    slug = models.SlugField('Atalho', max_length=200, null=True, blank=True)
    nome = models.CharField('Nome',max_length=30)
    sobrenome = models.CharField('Sobrenome',max_length=30, blank=True)
    email = models.CharField('E-mail',max_length=30, blank=True)
    telefone = models.CharField('Telefone',max_length=20)


    class Meta:
        verbose_name = ('Usuário')
        verbose_name_plural = ('Usuários')

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.nome[0:15].strip()

    def get_full_name(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        def get_id(self):
            return self.id





class Disciplina(models.Model):
    #usuarios = models.ManyToManyField(Usuario)
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
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name="linguagem")
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE, related_name="linguagem")
    STATUS_CHOICES=(
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )
    status = models.IntegerField('Situação', choices=STATUS_CHOICES,default=0,blank=True)








"""class Reserva(models.Model):
    #usuario = models.ManyToManyField(User)
    usuario = models.ManyToManyField(User)
    disciplina = models.ManyToManyField(Disciplina)
    STATUS_CHOICE = (
        (0, 'Pendente'),
        (1, 'Aprovdo'),
        (2, 'Cancelado')
    )
    status = models.IntegerField('Situação', choices=STATUS_CHOICE,default=0, blank=True)
    dataReserva = models.DateTimeField(auto_now_add=True)
    # usuario = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    #dataReserva = models.DateTimeField(auto_now_add=True)
    #horaFim = models.TimeField(verbose_name='Hora Início')
    #quantidade_dia = models.SmallIntegerField('Quantidades de dias ', default=6)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('usuario', 'disciplina'),)

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = ()"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import os
from PIL import Image
from django.utils.text import slugify
from django.db.models import Q, BooleanField
from django.utils import timezone


class Usuario(AbstractUser):
    slug = models.SlugField('Atalho', max_length=200, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20)
    is_staff = models.BooleanField(default=1)
    is_superuser = models.BooleanField(default=1)
    is_active = models.BooleanField(default=True)

    LOAN_STATUS = (
        ('professor', 'Professor'),
        ('aluno', 'Aluno'),

    )
    status = models.CharField(max_length=10,choices=LOAN_STATUS,blank=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Professor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="usuario")
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField('Descrição',max_length=255)
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

class Disciplina(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,related_name="professor")
    nome = models.CharField('Nome', max_length=50)
    titulo = models.CharField('Título', max_length=25)
    descricao_longa = models.TextField('Descrição')
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField('Atalho', unique=True, blank=True, null=True)
    data_reserva = models.DateTimeField('Data Início',default=timezone.now)

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
            slug = f'{slugify(self.titulo)}'
            self.slug = slug

        super().save(*args, **kwargs)

        def save(self, *args, **kwargs):
            if not self.id:
                id = f'{slugify(self.titulo)}'
                self.slug = id

            super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)


class UsuarioDisciplina(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="linguagem")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name="linguagem")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)


    LOAN_STATUS = (
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Cancelado', 'Cancelado')
    )
    status = models.CharField('Situação', max_length=12, default='Pendente', choices=LOAN_STATUS, blank=True)
    data_reserva = models.DateField('Data Reserva', null=True, blank=True)


    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        #unique_together = (('usuario','disciplina'),)


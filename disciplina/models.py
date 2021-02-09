from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os
from PIL import Image
from django.utils.text import slugify
from django.utils import timezone



class Professor(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/',blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    cpf = models.CharField(max_length=11,blank=True, null=True)
    telefone = models.CharField(max_length=15,blank=True, null=True)


    """def __str__(self):
        return f'{self.usuario}'"""

class Disciplina(models.Model):
    usuario = models.ManyToManyField(Usuario)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    titulo = models.TextField(max_length=25)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='disciplina_imagens/%Y/%m/',blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    data_reserva = models.DateTimeField(default=timezone.now)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size

        if(original_width <= new_width):
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

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
       return self.nome or self.professor

"""class Reserva(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    titulo = models.TextField(max_length=255)
    dataReserva = models.DateTimeField(auto_now_add=True)
    horaFim = models.TimeField(verbose_name='Hora Início')
    quantidade_dia = models.SmallIntegerField('Quantidades de dias ', default=6)

    def __str__(self):
         return self.nome"""

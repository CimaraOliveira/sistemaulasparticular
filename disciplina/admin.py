from django.contrib import admin
from . import models

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'titulo', 'professor', 'descricao_longa']


admin.site.register(models.Disciplina, DisciplinaAdmin)
admin.site.register(models.Professor)
admin.site.register(models.UsuarioDisciplina)




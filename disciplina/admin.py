from django.contrib import admin
from . import models

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'titulo', 'professor', 'descricao_longa']

class UsuarioDisciplinaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'disciplina', 'status']


admin.site.register(models.Disciplina, DisciplinaAdmin)
admin.site.register(models.Professor)
admin.site.register(models.UsuarioDisciplina,UsuarioDisciplinaAdmin)




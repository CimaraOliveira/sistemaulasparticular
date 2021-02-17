from django.contrib import admin

from disciplina.models import Usuario

class UserAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'telefone', 'user_choice']


admin.site.register(Usuario, UserAdmin)


from .models import Disciplina, UsuarioDisciplina
from django.db import models, connection

def getNrDisciplina(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT max(nr_Disciplina) nr_Disciplina FROM disciplinas_disciplina where user_id = %s", [user_id])
        row = directfectall(cursor)
        class Meta:
            model = Disciplina
            fields =  ['nr_disciplina']

    return row
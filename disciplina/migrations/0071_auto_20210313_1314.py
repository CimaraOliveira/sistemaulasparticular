# Generated by Django 3.1.6 on 2021-03-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0070_auto_20210313_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodisciplina',
            name='status',
            field=models.CharField(blank=True, choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=12, verbose_name='Situação'),
        ),
    ]

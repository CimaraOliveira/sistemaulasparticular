# Generated by Django 3.1.6 on 2021-03-15 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0075_usuariodisciplina_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariodisciplina',
            name='professor',
        ),
    ]
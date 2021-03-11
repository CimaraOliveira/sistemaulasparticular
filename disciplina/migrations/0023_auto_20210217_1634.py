# Generated by Django 3.1.6 on 2021-02-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0022_auto_20210217_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(default=-1, max_length=30, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_choice',
            field=models.CharField(choices=[('m', 'Adm'), ('p', 'Professor'), ('a', 'Aluno')], max_length=1),
        ),
    ]
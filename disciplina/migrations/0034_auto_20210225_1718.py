# Generated by Django 3.1.6 on 2021-02-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0033_auto_20210225_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user_choice',
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.BooleanField(blank=True, null=True, verbose_name='Tipo'),
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0020_delete_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariodisciplina',
            name='data_reserva',
            field=models.DateField(blank=True, null=True, verbose_name='Data Reserva'),
        ),
    ]
# Generated by Django 3.1.6 on 2021-03-17 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0087_auto_20210317_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodisciplina',
            name='professor',
            field=models.ForeignKey(blank=True, default=-1, on_delete=django.db.models.deletion.CASCADE, to='disciplina.professor'),
            preserve_default=False,
        ),
    ]
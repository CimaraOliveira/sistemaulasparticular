# Generated by Django 3.1.6 on 2021-03-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0051_auto_20210304_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
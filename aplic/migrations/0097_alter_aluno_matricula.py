# Generated by Django 4.2.6 on 2023-12-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0096_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=23292, unique=True, verbose_name='Matrícula'),
        ),
    ]

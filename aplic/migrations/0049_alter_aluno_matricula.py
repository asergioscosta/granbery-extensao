# Generated by Django 4.2.5 on 2023-10-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0048_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=35965, unique=True, verbose_name='Matrícula'),
        ),
    ]

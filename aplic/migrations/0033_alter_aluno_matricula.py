# Generated by Django 4.2.6 on 2023-10-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0032_remove_equipe_pessoa_equipe_aluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=50550, unique=True, verbose_name='Matrícula'),
        ),
    ]

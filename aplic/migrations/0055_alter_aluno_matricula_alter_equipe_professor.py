# Generated by Django 4.2.5 on 2023-10-17 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0054_alter_aluno_matricula_alter_equipe_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=43223, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.professor'),
        ),
    ]
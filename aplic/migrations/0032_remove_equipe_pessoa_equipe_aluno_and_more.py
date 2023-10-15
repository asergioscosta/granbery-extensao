# Generated by Django 4.2.6 on 2023-10-15 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0031_alter_aluno_matricula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='equipe',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aplic.aluno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=12881, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='ods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.ods'),
        ),
    ]

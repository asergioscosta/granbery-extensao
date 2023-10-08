# Generated by Django 4.2.6 on 2023-10-08 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=30, verbose_name='Nome da Instituição')),
                ('cnpj', models.CharField(max_length=11, verbose_name='CNPJ')),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
            },
        ),
        migrations.AddField(
            model_name='endereco',
            name='instituicao',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='aplic.instituicao'),
            preserve_default=False,
        ),
    ]

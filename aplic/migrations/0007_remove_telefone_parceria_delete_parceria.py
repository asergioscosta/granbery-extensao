# Generated by Django 4.2.6 on 2023-10-08 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0006_parceria_telefone_instituicao_telefone_parceria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefone',
            name='parceria',
        ),
        migrations.DeleteModel(
            name='Parceria',
        ),
    ]

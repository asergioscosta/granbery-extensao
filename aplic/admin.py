from django.contrib import admin

from aplic.models import Endereco, Professor, Aluno

# Register your models here.

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('area_atuacao',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula',) 
from django.contrib import admin

from aplic.models import Endereco, Professor, Aluno, Curso, Instituicao, Telefone, Parceria, Equipe, Projeto, Ods, Atividade

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

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome_instituicao', 'cnpj')

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo')

@admin.register(Parceria)
class ParceriaAdmin(admin.ModelAdmin):
   list_display = ('nome_parceria', 'cnpj', 'email')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'descricao')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome_equipe',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ano', 'periodo_realizacao', 'area_atuacao', 'resumo', 'justificativa', 'fundamentacao_teorica', 'metodologia', 'referencia', 'objetivos_gerais', 'resultados_esperados')

@admin.register(Ods)
class OdsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'carga_horaria', 'inicio_atividade', 'conclusao_atividade', 'objetivo', 'status')
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Pessoa(models.Model):
    sexos = (
         ("F", "Feminino"),
         ("M", "Masculino"),
         ("NB", "Não Binário")
    )
     
    nome = models.CharField(_('Nome'), max_length=30)
    sobrenome = models.CharField(_('Sobrenome'), max_length=40)
    cpf = models.CharField(_('CPF'), max_length=11)
    email = models.EmailField(_('E-mail'), blank=True, max_length=200)
    ata_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=('formato = dd/mm/aaaa'))
    sexo = models.CharField(max_length=2, blank=False, null=False, choices=sexos)

    class Meta:
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoa')

    def __str__(self):
        return self.nome
    
    
class Aluno(Pessoa):
    matricula = models.IntegerField(_('Matrícula'), unique=True)

    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')

    
class Professor(Pessoa):
    professor = (
        ('Professor', 'Professor'),
        ('Orientador', 'Orientador'),
    )

    area_atuacao = models.CharField(_('Área de Atuação'), max_length=30, blank=False, null=False, choices=professor)

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')

    def __str__(self):
        return self.area_atuacao

class Instituicao(models.Model):
    nome_instituicao = models.CharField(_('Nome da Instituição'), max_length=30)
    cnpj = models.CharField(_('CNPJ'), max_length=11)

    class Meta:
        verbose_name = _('Instituição')
        verbose_name_plural = _('Instituições')

    def __str__(self):
        return self.nome_instituicao
    
class Parceria(models.Model):
    nome_parceria = models.CharField(_('Nome da Parceria'), max_length=10)
    cnpj = models.CharField(_('CNPJ'), max_length=11)
    email = models.EmailField(_('E-mail'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Parceria')
        verbose_name_plural = _('Parcerias')

    def __str__(self):
        return self.nome_parceria

class Curso(models.Model):
    cursos = (
        ('Administração', 'Administração'),
        ('Sistemas de Informação', 'Sistemas de Informação'),
        ('Psicologia', 'Psicologia'),
        ('Direito', 'Direito'),
        ('Educação Física', 'Educação Física'),
    )
    nome_curso = models.CharField(_('Nome do Curso'), max_length=30, blank=False, null=False, choices=cursos)
    descricao = models.TextField(_('Descrição'), max_length=250)

    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.nome_curso

class Telefone(models.Model):
    telefone = (
    ('residencial', 'Telefone Residencial'),
    ('celular', 'Telefone Celular'),
    ('trabalho', 'Telefone Comercial')
    )

    numero = models.CharField(_('Número de Telefone'), max_length=20, blank=True, help_text=_('Formato: (xx) xxxxx-xxxx'))
    tipo = models.CharField('Tipo de Telefone', max_length=30, choices=telefone)
    
    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    parceria = models.ForeignKey(Parceria, null=False, on_delete=models.CASCADE)

    class Meta:
         verbose_name = _('Telefone')
         verbose_name_plural = _('Telefones')

    def __str__(self):
         return self.numero
    
class Endereco(models.Model):
    ufs = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    logradouro = models.CharField(_('Logradouro'), max_length=50)
    cep = models.CharField(_('CEP'), max_length=9)
    numero = models.CharField(_('Número'), max_length=10)
    complemento = models.CharField(_('Complemento'), blank=True, max_length=20)
    bairro = models.CharField(_('Bairro'), max_length=20)
    cidade = models.CharField(_('Cidade'), max_length=20)
    uf = models.CharField('UF', max_length=2, choices=ufs)

    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    parceria = models.ForeignKey(Parceria, null=False, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

class Projeto(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=255)
    ano = models.DateField(_('Data de Início do Projeto'), blank=True, null=True, help_text=('formato = dd/mm/aaaa'))
    periodo_realizacao = models.DateField(_('Data do Término do Projeto'), blank=True, null=True, help_text=('formato = dd/mm/aaaa'))
    area_atuacao = models.CharField(_('Área de Atuação'), max_length=100)
    resumo = models.TextField(_('Resumo'), max_length=255)
    justificativa = models.TextField(_('Justificativa'), max_length=255)
    fundamentacao_teorica = models.TextField(_('Fundamentação Teórica'), max_length=255)
    metodologia = models.TextField(_('Metodologia'), max_length=255)
    referencia = models.TextField(_('Referências'), max_length=255)
    objetivos_gerais = models.TextField(_('Objetivos Gerais'), max_length=255)
    resultados_esperados = models.TextField(_('Resultados Esperados'), max_length=255)

    class Meta:
        verbose_name = _('Projeto')
        verbose_name_plural = _('Projetos')

    def __str__(self):
        return self.nome
    
class Equipe(models.Model):
    nome_equipe = models.CharField(_('Nome da Equipe'), max_length=30)

    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Equipe')
        verbose_name_plural = _('Equipes')

    def __str__(self):
        return self.nome_equipe 
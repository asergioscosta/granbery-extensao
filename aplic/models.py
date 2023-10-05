from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Pessoa(models.Model):
    sexos = (
         ("F", "Feminino"),
         ("M", "Masculino"),
         ("O", "Outros")
    )
     
    nome = models.CharField(_('Nome'), max_length=30)
    sobrenome = models.CharField(_('Sobrenome'), max_length=40)
    cpf = models.CharField(_('CPF'), max_length=11)
    email = models.EmailField(_('E-mail'), blank=True, max_length=200)
    ata_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=('formato = dd/mm/aaaa'))
    sexo = models.CharField(max_length=1, blank=False, null=False, choices=sexos)

    class Meta:
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoa')

    def __str__(self):
        return self.nome
    
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

    cep = models.CharField(_('CEP'), max_length=9)
    logradouro = models.CharField(_('Logradouro'), max_length=50)
    numero = models.CharField(_('Número'), max_length=10)
    complemento = models.CharField(_('Complemento'), blank=True, max_length=20)
    bairro = models.CharField(_('Bairro'), max_length=20)
    cidade = models.CharField(_('Cidade'), max_length=20)
    uf = models.CharField('UF', max_length=2, choices=ufs)

    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

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
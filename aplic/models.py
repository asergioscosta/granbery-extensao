from django.db import models
import random
from stdimage.models import StdImageField
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

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
    data_nascimento = models.DateField(_('Data de Nascimento'), blank=True, null=True, help_text=('formato = dd/mm/aaaa'))
    sexo = models.CharField(max_length=2, blank=False, null=False, choices=sexos)

    class Meta:
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoa')

    def __str__(self):
        return self.nome

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    
class Instituicao(models.Model):
    nome_instituicao = models.CharField(_('Nome da Instituição'), max_length=30)
    cnpj = models.CharField(_('CNPJ'), max_length=11)

    class Meta:
        verbose_name = _('Instituição')
        verbose_name_plural = _('Instituições')

    def __str__(self):
        return self.nome_instituicao

class Parceria(models.Model):
    nome_parceria = models.CharField(_('Nome da Parceria'), max_length=100)
    cnpj = models.CharField(_('CNPJ'), max_length=11)
    email = models.EmailField(_('E-mail'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Parceria')
        verbose_name_plural = _('Parcerias')

    def __str__(self):
        return self.nome_parceria
        
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
    
    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    parceria = models.ForeignKey(Parceria, null=False, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    def __str__(self):
        return self.logradouro

class Telefone(models.Model):
    telefone = (
    ('residencial', 'Telefone Residencial'),
    ('celular', 'Telefone Celular'),
    ('trabalho', 'Telefone Comercial')
    )

    numero = models.CharField(_('Número de Telefone'), max_length=20, blank=True, help_text=_('Formato: (xx) xxxxx-xxxx'))
    tipo = models.CharField('Tipo de Telefone', max_length=30, choices=telefone)

    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)
    parceria = models.ForeignKey(Parceria, null=False, on_delete=models.CASCADE)

    class Meta:
         verbose_name = _('Telefone')
         verbose_name_plural = _('Telefones')

    def __str__(self):
         return self.numero

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
    
class Equipe(models.Model):
    nome_equipe = models.CharField(_('Nome da Equipe'), max_length=30)

    professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Equipe')
        verbose_name_plural = _('Equipes')

    def __str__(self):
        return self.nome_equipe 


class Aluno(Pessoa):
    matricula = models.IntegerField(_('Matrícula'), unique=True, default=random.randint(10000, 99999))

    equipe = models.ForeignKey(Equipe, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')

    def __str__(self):
        return str(self.matricula)

class Curso(models.Model):
    nome_curso = models.CharField(_('Nome do Curso'), max_length=30, blank=False, null=False)
    descricao = models.TextField(_('Descrição'), max_length=30)
    Instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    imagem = StdImageField(_('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})
    professor = models.ManyToManyField(Professor)
    aluno = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.nome_curso

class Ods(models.Model):
    ods = (
        ('Ods 1', 'ODS 1 - Erradicação da pobreza'),
        ('Ods 2', 'ODS 2 - Fome zero e agricultura sustentável'),
        ('Ods 3', 'ODS 3 - Saúde e bem-estar'),
        ('Ods 4', 'ODS 4 - Educação de qualidade'),
        ('Ods 5', 'ODS 5 - Igualdade de gênero'),
        ('Ods 6', 'ODS 6 - Água potável e saneamento'),
        ('Ods 7', 'ODS 7 - Energia limpa e acessível'),
        ('Ods 8', 'ODS 8 - Trabalho decente e crescimento econômico'),
        ('Ods 9', 'ODS 9 - Indústria, inovação e infraestrutura'),
        ('Ods 10', 'ODS 10 - Redução das desigualdades'),
        ('Ods 11', 'ODS 11 - Cidades e comunidades sustentáveis'),
        ('Ods 12', 'ODS 12 - Consumo e produção responsáveis'),
        ('Ods 13', 'ODS 13 - Ação contra a mudança global do clima'),
        ('Ods 14', 'ODS 14 - Vida na água'),
        ('Ods 15', 'ODS 15 - Vida terrestre'),
        ('Ods 16', 'ODS 16 - Paz, Justiça e Instituições Eficazes'),
        ('Ods 17', 'ODS 17 - Parcerias e meios de implementação'),
    )

    descricao_ods = (

        ('ODS 1 - Erradicação da pobreza', 'O ODS 1 busca eliminar a pobreza em todas as suas formas e em todos os lugares, garantindo que todas as pessoas tenham acesso a recursos básicos e oportunidades para uma vida digna.'),
        ('ODS 2 - Fome zero e agricultura sustentável', 'O ODS 2  visa acabar com a fome, garantindo o acesso a alimentos seguros e nutritivos para todos, ao mesmo tempo em que promove práticas agrícolas sustentáveis.'),
        ('ODS 3 - Saúde e bem-estar', 'O ODS 3 concentra-se em assegurar uma vida saudável e promover o bem-estar para todas as idades, com metas que incluem reduzir a mortalidade infantil e melhorar o acesso a serviços de saúde.'),
        ('ODS 4 - Educação de qualidade', 'O ODS 4 visa garantir uma educação inclusiva, equitativa e de qualidade para todos, promovendo oportunidades de aprendizado ao longo da vida.'),
        ('ODS 5 - Igualdade de gênero', 'O ODS 5 busca alcançar a igualdade de gênero e empoderar todas as mulheres e meninas, promovendo a igualdade de oportunidades e o fim da discriminação de gênero.'),
        ('ODS 6 - Água potável e saneamento', 'O ODS 6 visa garantir o acesso universal a água potável segura e saneamento adequado, contribuindo para a saúde e o bem-estar das comunidades.'),
        ('ODS 7 - Energia limpa e acessível', 'O ODS 7 busca garantir o acesso universal a energia acessível, confiável, sustentável e moderna, promovendo o desenvolvimento econômico e a mitigação das mudanças climáticas.'),
        ('ODS 8 - Trabalho decente e crescimento econômico', 'O ODS 8 visa promover o crescimento econômico sustentável, emprego digno e produtivo, e trabalho decente para todos.'),
        ('ODS 9 - Indústria, inovação e infraestrutura', 'O ODS 9 concentra-se na construção de infraestruturas resilientes, na promoção da industrialização sustentável e na inovação tecnológica.'),
        ('ODS 10 - Redução das desigualdades', 'O ODS 10 busca reduzir as desigualdades dentro e entre os países, promovendo a inclusão social e econômica.'),
        ('ODS 11 - Cidades e comunidades sustentáveis', 'O ODS 11 visa tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis, promovendo uma urbanização planejada.'),
        ('ODS 12 - Consumo e produção responsáveis', 'O ODS 12 promove padrões de consumo e produção sustentáveis, buscando reduzir o desperdício de recursos naturais e minimizar os impactos ambientais.'),
        ('ODS 13 - Ação contra a mudança global do clima', 'O ODS 13 visa tomar medidas urgentes para combater as mudanças climáticas e seus impactos, incluindo a mitigação e adaptação.'),
        ('ODS 14 - Vida na água', 'O ODS 14 se concentra na conservação e uso sustentável dos oceanos, mares e recursos marinhos, para proteger a biodiversidade marinha.'),
        ('ODS 15 - Vida terrestre', 'O ODS 15 busca proteger, restaurar e promover o uso sustentável dos ecossistemas terrestres, gerenciar de forma sustentável florestas e combater a desertificação.'),
        ('ODS 16 - Paz, Justiça e Instituições Eficazes', 'O ODS 16 busca promover sociedades pacíficas, justas e inclusivas, fortalecendo as instituições para a promoção da paz e da justiça.'),
        ('ODS 17 - Parcerias e meios de implementação', 'O ODS 17 é sobre fortalecer os meios de implementação e revitalizar a parceria global para o desenvolvimento sustentável.'),
    )
    nome = models.CharField(_('Nome da ODS'), max_length=6, choices=ods)
    descricao = models.TextField(_('Descrição'), max_length=255, choices=descricao_ods)

    class Meta:
        verbose_name = _('ODS')
        verbose_name_plural = _('ODSs')

    def __str__(self):
        return self.nome
    
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

    parceria = models.ManyToManyField(Parceria)
    ods = models.ManyToManyField(Ods)
    equipe = models.ForeignKey(Equipe, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Projeto')
        verbose_name_plural = _('Projetos')

    def __str__(self):
        return self.nome
        
        
class Atividade(models.Model):
    atividade = (
         ('Realizado', 'Realizado'),
         ('A Realizar', 'A Realizar'),
         ('Em Andamento', 'Em Andamento'),
)

    descricao = models.TextField(_('Descrição'), max_length=255)
    carga_horaria = models.PositiveIntegerField(_('Carga Horária'))
    inicio_atividade = models.DateField(_('Início da Atividade'))
    conclusao_atividade = models.DateField(_('Conclusão da Atividade'), null=True, blank=True)
    objetivo = models.TextField(_('Objetivo'), max_length=255)
    status = models.CharField('Status', max_length=20, choices=atividade)

    projeto = models.ForeignKey(Projeto, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Atividade')
        verbose_name_plural = _('Atividades')

    def __str__(self):
        return self.descricao
    

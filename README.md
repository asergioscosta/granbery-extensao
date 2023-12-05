# Granbery Extensao

### Índice

- [Descrição do Projeto](#descrição-do-projeto)

- [Requisitos](#requisitos)

- [Funcionalidades](#funcionalidades)

- [Técnicas e Tecnologias Utilizadas](#técnicas-e-tecnologias-utilizadas)

- [Acesso ao Projeto](#acesso-ao-projeto)

- [Abrir e Executar o Projeto](#abrir-e-executar-o-projeto)

- [Desenvolvedores](#desenvolvedores)


## Descrição do Projeto

O objetivo do projeto é criar um sistema para armazenar todos os projetos da disciplina de
Extensão Universitária da Faculdade Metodista Granbery. O sistema proporcionará aos usuários a
possibilidade de pesquisar os projetos por equipes, orientadores, alunos, parcerias etc. Além disso
será possível localizar por palavras chave e visualizar vídeos e fotos das apresentações.
Os projetos serão armazenados em um banco de dados acessado pelos orientadores, que serão
responsáveis por aprovar ou não os projetos, de acordo com as diretrizes estabelecidas pelas ODS
(Objetivos de Desenvolvimento Sustentável) e pelo PiEX (Programas Interinstitucionais de
Extensão).

## Requisitos

### Requisitos Funcionais do Sistema

**`Administrador:`**
- O Sistema deve permitir realizar cadastro do aluno, orientador e cliente no sistema.
- O Sistema deve permitir cadastrar as parcerias.

**`Administrador, Aluno, Orientador e Cliente:`**
- O Sistema deve permitir efetuar Login.
- O sistema deve dar a opção de esquecer a senha.
- O Sistema deve permitir avaliar os projetos.
- O Sistema deve permitir comentar nos projetos.

**`Administrador, Aluno e Orientador :`**
- O Sistema deve permitir cadastrar projetos.
- O Sistema deve permitir editar os projetos.
- O Sistema deve permitir armazenar as fotos e vídeos das apresentações dos projetos.

**`Administrador e Orientador:`**
- O Sistema deve permitir excluir os projetos.
- O Sistema deve permitir cadastrar as equipes dos projetos.
- O Sistema deve permitir gerar relatórios.
- O Sistema deve permitir cadastrar as ODS (Objetivos de Desenvolvimento Sustentável).

### Requisitos Não Funcionais do Sistema

- O sistema deve ter um mecanismo de bloqueio de conta de usuário por 3 minutos após três tentativas de autenticação com informações de usuário ou senha inválidas.

- A interface do usuário deve ser intuitiva e fácil de usar para garantir uma boa experiência do usuário.

- O sistema deve ser otimizado para carregar rapidamente, com um tempo médio de carregamento da página de menos de 20 segundos.

- O sistema deve estar em conformidade com regulamentações da LGPD.

- O sistema deve ser compatível com os principais navegadores da web.

- O sistema deve ser capaz de escalonar para gerenciar um grande volume de dados à medida que mais projetos são adicionados ao sistema.

- O sistema deve oferecer um painel de administração intuitivo para que os administradores possam gerenciar facilmente o conteúdo e as configurações do sistema.

- O sistema deve ter um mecanismo de bloqueio de conta de usuário por 3 minutos após três tentativas de autenticação com informações de usuário ou senha inválidas.

- A interface do usuário deve ser intuitiva e fácil de usar para garantir uma boa experiência do usuário.

## Funcionalidades

1. **Cadastrar Projeto:**
- O administrador, aluno e orientador acessam o sistema por meio do login para cadastrar um novo projeto de Extensão Universitária.
- O sistema solicita informações essenciais do projeto, como título, descrição e datas relevantes.
- Após a validação do orientador, o projeto é registrado no sistema.

2. **Editar Projeto:**
- O administrador, aluno e orientador acessam o sistema por meio do login e vão até o projeto de Extensão Universitária desejado.
- Realizam as alterações necessárias e salvam as atualizações.

3. **Excluir Projeto:**
- O administrador e orientador acessam o sistema por meio do login e vão até o projeto de Extensão Universitária desejado.
- Selecionam o projeto a ser removido e confirmam a exclusão.
- O sistema atualiza o banco de dados para refletir a remoção.

4. **Cadastrar Parceria:**
- O administrador e orientador acessam o sistema por meio do login e inserem informações sobre uma nova parceria com outra instituição ou organização.
- O sistema coleta detalhes da parceria, como nome e informações de contato.
- Após a validação, a parceria é registrada.

5. **Cadastrar Equipe do Projeto:**
- O administrador e orientador acessam o sistema por meio do login e cadastram as equipes de projetos.
- Incluem membros da equipe, funções e informações de contato.
- O sistema registra as informações da equipe associada a um projeto específico.

6. **Cadastrar Orientador:**
- O administrador acessa o sistema por meio do login e insere informações sobre novos orientadores.
- Inclui dados como área de atuação, histórico acadêmico e informações de contato.
- Os orientadores são associados a projetos relevantes.

7. **Pesquisar Projetos:**
- Administrador, aluno, orientador, visitante e parceria podem aplicar filtros de pesquisa para encontrar projetos com base em critérios como área de atuação, objetivos, status e período de execução.

8. **Gerar Relatórios:**
- O administrador e orientador acessam o sistema por meio do login e geram relatórios sobre o desempenho dos projetos.
- Eles selecionam os parâmetros desejados e o sistema cria relatórios que incluem métricas e dados relevantes.

9. **Avaliar Projeto:**
- O administrador, aluno, orientador, visitante e parceria têm a opção de avaliar os projetos.

10. **Comentários:**
- O administrador, aluno, orientador, visitante e parceria podem deixar comentários em projetos.
- Para realizar um comentário, é necessário utilizar a opção de busca ou acessar a seção de projetos e selecionar o projeto desejado.
- Os comentários são diretamente associados ao projeto e podem ser visualizados por todos os usuários.

11. **Cadastrar ODS:**
- O administrador e orientador acessam o sistema por meio do login e inserem informações sobre Objetivos de Desenvolvimento Sustentável (ODS) relacionados aos projetos.

12. **Armazenar Fotos e Vídeos:**
- O sistema permite o armazenamento e exibição de fotos e vídeos relacionados às apresentações dos projetos.

## Técnicas e Tecnologias Utilizadas

- **Linguagem de Programação:** ``HTML``, ``CSS``, ``JavaScript``, ``Python`` e ``Django``
- **Ambiente de Desenvolvimento:** ``Visual Studio Code``
- **Sistema Gerenciador de Banco de Dados (SGBD):** ``MySQL``
- **Ferramentas de Controle de Versão:** ``GitHub``
- **Documentação:** 

## Acesso ao Projeto

Você pode acessar os arquivos do projeto [clicando aqui](https://github.com/asergioscosta/granbery-extensao) ou [baixá-lo como um arquivo zip](https://github.com/asergioscosta/granbery-extensao/archive/refs/heads/main.zip).

## Abrir e Executar o Projeto

1. Escolha uma pasta para criar o projeto. Ex.: ``d:\nome_pasta``
2. Crie um repositório no GitHub.
3. Clone o repositório usando o comando ``git clone <URL_do_repositorio>``.
4. Crie um ambiente virtual usando o comando ``python -m venv venv``.
5. Ative o ambiente virtual com o comando ``venv\Scripts\Activate``.
6. Instale o Django usando o comando ``pip install django``.
7. Instale o pacote ``django-bootstrap-v5`` com o comando ``pip install django-bootstrap-v5``.
8. Verifique a versão do Django com o comando ``python -m django --version``.
9. Verifique a versão do Python com o comando ``python --version``.
10. Inicie um novo projeto Django com o comando ``django-admin startproject nome-projeto``.
11. Entre na pasta do projeto usando o comando ``cd sca``.
12. Execute as migrações iniciais do banco de dados com o comando ``python manage.py makemigrations`` e em seguida execute o comando ``python manage.py migrate``.
13. Crie um superusuário com o comando `python manage.py createsuperuser`.
    - Execute `python -m ensurepip --default-pip` se ocorrer um erro com o pip.
14. Dentro do Visual Studio Code, abra o terminal (command).
15. Crie um aplicativo Django com o comando `python manage.py startapp aplic`.
16. Dentro do diretório `aplic`, crie o arquivo `urls.py`.
17. Configure o arquivo `urls.py` do projeto para incluir o `urls.py` do aplicativo.
18. Crie o diretório `templates` dentro do diretório `aplic` para armazenar os templates HTML da aplicação.
19. Crie o arquivo `index.html` dentro do diretório `templates`. Este será a página inicial da aplicação.
20. Configure o arquivo `views.py` do aplicativo para renderizar o `index.html`.
21. Crie um banco de dados chamado `sca` no PostgreSQL.
22. Configure o arquivo `settings.py` para se conectar ao PostgreSQL.

## Desenvolvedores

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/102989796?v=4" width=115>](https://github.com/asergioscosta)  |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/114194728?v=4" width=115>](https://github.com/eduardocarlosd)  |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/101905481?v=4" width=115>](https://github.com/DVDuarte)

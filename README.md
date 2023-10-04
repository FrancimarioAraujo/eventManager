# eventManager
Repositório do projeto de Engenharia de Software II e Gerenciamento de Projetos

O **eventManager** é uma plataforma de gestão de eventos que atende a dois perfis de usuários distintos: o **usuário padrão**, habilitado para visualizar os eventos e adquirir ingressos, e o **Promoter**, com permissão para criar e administrar seus próprios eventos. Este projeto visa proporcionar uma experiência intuitiva e eficiente para ambos os grupos de usuários, atendendo às suas necessidades específicas e oferecendo funcionalidades personalizadas para suas respectivas atividades na plataforma.

## Funcionalidades
- **Cadastro de Usuário:** Os usuários podem se cadastrar como "Comum" ou "Promoter" no site.
- **Autenticação:** Login e logout de usuários.
- **Visualização de Eventos:** Os usuários comuns podem ver eventos disponíveis.
- **Compra de Ingressos:** Os usuários comuns podem comprar ingressos para eventos.
- **Gerenciamento de Eventos:** Os promoters podem criar, editar e excluir eventos.
- **Promoção de Eventos:** Os promoters podem promover seus eventos, tornando-os visíveis para os usuários comuns.
  
## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- **project/**
  - Pasta raiz do projeto Django.
  
- **register/**
  - Aplicação Django para o cadastro de usuários.
  
- **login/**
  - Aplicação Django para o login dos usuários.

 ## Configuração do Banco de Dados

Este projeto utiliza o banco de dados PostgreSQL. Para configurar a conexão com o banco de dados, siga os passos abaixo:

1. Abra o arquivo `settings.py` localizado na pasta `eventManager/eventManager/`.

2. Localize a seção `DATABASES` e configure as credenciais do banco de dados PostgreSQL conforme o exemplo abaixo:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nome_do_banco_de_dados',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',   # ou o endereço do seu servidor PostgreSQL
           'PORT': '',             # porta do PostgreSQL (opcional)
       }
   }
    
## Como Executar o Projeto

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local:

1. Clone o repositório:

    ```bash
    git clone https://github.com/FrancimarioAraujo/eventManager.git

2. Crie um ambiente virtual

    ```bash
    python -m venv venv
    venv\Scripts\activate # Ativação Windows
    source venv/bin/activate # Ativação no Linux

3. Instale as dependências:
    ```bash
    pip install - r requirements.txt

4. Aplique as migrações para criar o banco de dados inicial:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
   
5. Inice o servidor:

    ```bash
       python manage.py runserver

6. O site estará disponível em http://127.0.0.1:8000/. Você pode acessar a aplicação e começar a explorar suas funcionalidades.

## Tecnologia Utilizadas
- Django: versão 4.2.4
- Python: versão 3.11.4




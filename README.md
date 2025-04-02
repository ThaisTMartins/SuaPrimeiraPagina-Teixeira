# Como Executar

## Ativar o ambiente virtual
`.\SuaPrimeiraPagina+Teixeira\Scripts\activate`

## Criar o banco de dados
`python manage.py makemigrations`
`python manage.py migrate`

## Criar o usuário admin
`python manage.py createsuperuser`
Adicione o nome de usuário e senha que serão utilizados para acessar a área de administrador do sistema.

## Popular o banco de dados
`python populate.py`

## Executar o servidor
`python manage.py runserver`

# Objetivo da Aplicação

A aplicação simula um site com informações cadastrais de cliente. Para isso, há 3 tabelas relacionais.

## Tabelas do Banco

| Usuario      |
|--------------|
| **id**       |
| nome         |
| senha        |

| Cliente           |
|-------------------|
| id                |
| **id_usuario**    |
| cpf               |
| telefone          |
| email             |
| ano_nascimento    |

| Interesses        |
|-------------------|
| id                |
| **id_cliente**    |
| interesse         |

## Interfaces

As interfaces são dependentes entre si, seguindo a relação apontada nas tabelas do banco de dados. Dessa forma, os seguintes passos de cadastro devem ser seguidos:

1) Cadastro de usuário;
2) Cadastro de cliente, associado ao id_usuario;
3) Cadastro de interesses, associado ao id_cliente;

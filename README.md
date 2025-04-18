# Como Executar

## Ativar o ambiente virtual
`.\SuaPrimeiraPagina+Teixeira\Scripts\activate`

## Criar o banco de dados
`python manage.py makemigrations`
`python manage.py migrate`

## Popular o banco de dados
Um arquivo foi criado com alguns cadastros, para possibilitar uma visualização mais rápida do funcionamento da aplicação. Se deseja inserir todos os dados manualmente, não execute o comando abaixo:
`python populate.py`

## Criar o usuário admin
`python manage.py createsuperuser`
Adicione o nome de usuário e senha que serão utilizados para acessar a área de administrador do sistema. Caso deseje adicionar manualmente, além dois itens que foram incluídos no arquivo populate.py.

## Adicionar as dependências
`pip install -r requirements.txt`

## Executar o servidor
`python manage.py runserver`

# Objetivo da Aplicação

A aplicação simula um site com informações cadastrais de cliente. Para isso, há 3 tabelas relacionais.

## Tabelas do Banco

## Modelos de Banco de Dados

| **Usuario** | **Cliente** | **Categoria** | **Produto** | **Interesse** | **Avatar** |
|-------------|-------------|---------------|-------------|---------------|------------|
| **id**      | **id**      | **id**        | **id**      | **id**        | **id**     |
| username    | nome        | categoria     | produto     | cliente       | Usuario    |
| password    | sobrenome   |               | descricao   | interesse     | imagem     |
| tipo_usuario| cpf         |               | ano_fabricacao|              |            |
|             | email       |               | nome_categoria|              |            |
|             | data_nascimento|           | data_publicacao|             |            |
|             | telefone    |               | preco       |               |            |
|             | usuario     |               | status      |               |            |
|             |             |               | quantidade  |               |            |
|             |             |               | data_modificao|             |            |
|             |             |               | autor_modificacao|          |            |


Além dessas tabelas, existe uma chamada Produto, que indica os produtos disponíveis na plataforma:

| Produtos          |
|-------------------|
| id                |
| produto           |
| quantidade        |

## Interfaces

As interfaces são dependentes entre si, seguindo a relação apontada nas tabelas do banco de dados. Dessa forma, os seguintes passos de cadastro devem ser seguidos:

1) Cadastro de usuário, apenas na página de admin do django ou diretamente pela aplicação, após login de admin;
2) Cadastro de cliente, associado ao id_usuario;
3) Cadastro de interesses, associado ao id_cliente;
4) Cadastro de produtos, apenas na página de admin do django ou diretamente pela aplicação, após login de admin;

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

As bibliotecas utilizadas foram Django, Djano-widget-tweaks e Pillow. O arquivo requirementes.txt possui todas as dependências necessárias para execução do projeto.

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

As tabelas Usuário, Cliente e Interesse se relacionam diretamente no seguinte fluxo Usuário -> Cliente -> Interesse. Além disso, um Avatar é atribuído ao usuário.

A tabela de Produtos tem relação com Categoria.

## Interfaces

As interfaces são dependentes entre si, seguindo a relação apontada nas tabelas do banco de dados. Dessa forma, os seguintes passos de cadastro devem ser seguidos:

1) Registro de usuário, diretamente pela aplicação, independentemente de ter sido realizado um login;
2) Cadastro de cliente, associado ao id_usuario;
3) Cadastro de interesses, associado ao id_cliente;
4) Cadastro de categoria, para que possa ser associada a um produto;
5) Cadastro de produtos;

Todos os itens possuem o padrão CRUD, no entanto as permissões para edição e exclusão dependem do tipo de permissão do usuário.

## Testes

Não foi criado um arquivo de teste, no entanto foram realizadas manipulações na interface de maneira manual para validar o funcionamento.

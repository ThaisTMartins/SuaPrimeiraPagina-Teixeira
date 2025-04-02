# Como Executar

## Popular o banco de dados
Execute o comando:

python populate.py

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

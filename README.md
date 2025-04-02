# SuaPrimeiraPagina-Teixeira

A aplicação simula um site com informações cadastrais de cliente. Para isso, há 3 tabelas relacionais:

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

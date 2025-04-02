# SuaPrimeiraPagina-Teixeira

A aplicação simula um site com informações cadastrais de cliente. Para isso, há 3 tabelas relacionais:

### Tabela: Usuario
| **<span style="color:blue">id</span>** | nome          | senha          |
|--------------------------|---------------|---------------|

### Tabela: Cliente
| id | **<span style="color:blue">id_usuario</span>** | cpf           | telefone        | email           | ano_nascimento  |
|---------------------------|---------------|----------------|-----------------|-----------------|

### Tabela: Interesses
| id | **<span style="color:red">id_cliente</span>** | interesse |
|--|---------------------------|---------------|

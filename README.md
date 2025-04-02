# SuaPrimeiraPagina-Teixeira

A aplicação simula um site com informações cadastrais de cliente. Para isso, há 3 tabelas relacionais:

<div style="display: flex; gap: 20px;">

<!-- Tabela Usuario -->
<table>
  <thead>
    <tr>
      <th>Usuario</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b style="color:blue;">id</b></td>
    </tr>
    <tr>
      <td>nome</td>
    </tr>
    <tr>
      <td>senha</td>
    </tr>
  </tbody>
</table>

<!-- Tabela Cliente -->
<table>
  <thead>
    <tr>
      <th>Cliente</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b style="color:red;">id_usuario</b></td>
    </tr>
    <tr>
      <td>cpf</td>
    </tr>
    <tr>
      <td>telefone</td>
    </tr>
    <tr>
      <td>email</td>
    </tr>
    <tr>
      <td>ano_nascimento</td>
    </tr>
  </tbody>
</table>

<!-- Tabela Interesses -->
<table>
  <thead>
    <tr>
      <th>Interesses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b style="color:red;">id_cliente</b></td>
    </tr>
    <tr>
      <td>outro_campo1</td>
    </tr>
    <tr>
      <td>outro_campo2</td>
    </tr>
  </tbody>
</table>

</div>


# SuaPrimeiraPagina-Teixeira

A aplicação simula um site com informações cadastrais de cliente. Para isso, há 3 tabelas relacionais:
<div style="display: flex; gap: 20px;">

  <!-- Tabela Usuario -->
  <table border="1" style="border-collapse: collapse; text-align: center;">
    <tr>
      <th>Usuario</th>
    </tr>
    <tr>
      <td><span style="color:blue; font-weight:bold;">id</span></td>
    </tr>
    <tr>
      <td>nome</td>
    </tr>
    <tr>
      <td>senha</td>
    </tr>
  </table>

  <!-- Tabela Cliente -->
  <table border="1" style="border-collapse: collapse; text-align: center;">
    <tr>
      <th>Cliente</th>
    </tr>
    <tr>
      <td><span style="color:red; font-weight:bold;">id_usuario</span></td>
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
  </table>

  <!-- Tabela Interesses -->
  <table border="1" style="border-collapse: collapse; text-align: center;">
    <tr>
      <th>Interesses</th>
    </tr>
    <tr>
      <td><span style="color:red; font-weight:bold;">id_cliente</span></td>
    </tr>
    <tr>
      <td>outro_campo1</td>
    </tr>
    <tr>
      <td>outro_campo2</td>
    </tr>
  </table>

</div>

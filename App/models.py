from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser): # Optei por fazer um usuário personalizado, para que eu possa usar os campos conforme minhas entregas antigas
    class TipoUsuario(models.TextChoices):
        administrador = 'A', 'Administrador'
        cliente = 'C', 'Cliente'
    tipo_usuario = models.CharField(max_length=1, choices=TipoUsuario.choices, default=TipoUsuario.cliente) # Tipo de usuário, padrão cliente
    # Não é necessário definir password e username, pois já estão definidos no AbstractUser

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='clientes') # cascade, vai deletar tudo que estiver associado, no caso os interesses
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True) # CPF único, não pode ter dois iguais
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField()
    telefone = models.IntegerField()

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria  # Mostra o nome da categoria no dropdown

class Produto(models.Model):
    class Status(models.TextChoices):
        disponivel = 'D', 'Disponível'
        vendido = 'V', 'Vendido'
        reposicao = 'R', 'Reposição'
    produto = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    ano_fabricacao = models.IntegerField()
    nome_categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, related_name='produtos') # Protege a categoria, não deixa deletar se tiver produtos associados
    data_publicacao = models.DateTimeField(auto_now_add=True) # Adiciona a data de publicação automaticamente
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Preço do produto, com 10 dígitos no total e 2 depois da vírgula
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.disponivel)
    quantidade = models.IntegerField(default=1) # Quantidade do produto, padrão 1
    data_modificao = models.DateTimeField(auto_now=True) # Adiciona a data de modificação automaticamente
    autor_modificacao = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

class Interesse(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='interesses')
    interesse = models.CharField(max_length=100)

class Avatar(models.Model):
    Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagem}"
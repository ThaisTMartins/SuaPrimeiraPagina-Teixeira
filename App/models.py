from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=8)

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='clientes') # cascade, vai deletar tudo que estiver associado, no caso os interesses
    email = models.EmailField(max_length=50)
    ano_nascimento = models.IntegerField()
    telefone = models.IntegerField()
    cpf = models.IntegerField()

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria  # Mostra o nome da categoria no dropdown

class Produto(models.Model):
    produto = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    ano_fabricacao = models.IntegerField()
    nome_categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, related_name='produtos') # Protege a categoria, não deixa deletar se tiver produtos associados

class Interesse(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='interesses')
    interesse = models.CharField(max_length=100)

# Usada para trazer informações adicionais no banco de dados
# class Post(models.Model):
#     titulo = models.CharField(max_length=200)
#     conteudo = models.TextField()
#     data_publicacao = models.DateTimeField(auto_now_add = True)

#     def __str__(self):
#         return self.titulo

class Avatar(models.Model):
    Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagem}"
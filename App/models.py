from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=8)

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=8)
    email = models.EmailField(max_length=50)
    ano_nascimento = models.IntegerField()
    telefone = models.IntegerField()
    cpf = models.IntegerField()
    interesses = models.CharField(max_length=200)

class Produto(models.Model):
    produto = models.CharField(max_length=1000)

# Usada para trazer informações adicionais no banco de dados
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.titulo
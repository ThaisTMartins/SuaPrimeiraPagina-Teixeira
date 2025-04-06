# Esse arquivo irá popular o banco de dados com dados simulados para que seja mais fácil verificar o funcionamento da aplicação

import os
import django

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SuaPrimeiraPagina.settings')
django.setup()

from App.models import Usuario, Cliente, Produto, Interesse  

def popular_banco():
    # Criação de usuários
    usuario1 = Usuario.objects.create(nome="João", senha="12345678")
    usuario2 = Usuario.objects.create(nome="Maria", senha="87654321")

    # Criação de clientes (relacionados aos usuários)
    cliente1 = Cliente.objects.create(usuario=usuario1, email="joao@email.com", ano_nascimento=1990, telefone=123456789, cpf=11122233344)
    cliente2 = Cliente.objects.create(usuario=usuario2, email="maria@email.com", ano_nascimento=1985, telefone=987654321, cpf=55566677788)

    # Criação de produtos
    produto1 = Produto.objects.create(produto="Notebook Gamer")
    produto2 = Produto.objects.create(produto="Smartphone")

    # Criação de interesses (dois interesses para cliente1)
    Interesse.objects.create(cliente=cliente1, interesse="TV")
    Interesse.objects.create(cliente=cliente1, interesse="Case")
    Interesse.objects.create(cliente=cliente2, interesse="Headset")

    print("Dados populados com sucesso!")

if __name__ == '__main__':
    popular_banco()


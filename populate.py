# Esse arquivo irá popular o banco de dados com dados simulados para que seja mais fácil verificar o funcionamento da aplicação
import os
import django

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SuaPrimeiraPagina.settings')
django.setup()

from App.models import Usuario, Cliente, Produto, Interesse, Categoria

def popular_banco():
    # Usuário administrador padrão do sistema
    admin_padrao = Usuario.objects.create_user(
        password='admin',
        username='admin',
        tipo_usuario='A',
        is_superuser=True,
        is_staff=True
    )
    admin_padrao.save()

    # Usuário administrador (Gabriel)
    admin_gabriel = Usuario.objects.create_user(
        password='123456',
        username='Gabriel',
        tipo_usuario='A',
        is_superuser=True,
        is_staff=True
    )
    admin_gabriel.save()

    # Usuários clientes
    user1 = Usuario.objects.create_user(
        password='123456',
        username='jsouza1',
        tipo_usuario='C'
    )
    user2 = Usuario.objects.create_user(
        password='123456',
        username='cferreira1',
        tipo_usuario='C'
    )

    # Clientes relacionados
    cliente1 = Cliente.objects.create(
        usuario=user1,
        nome ='Joana',
        sobrenome='Souza',
        cpf='22222222222',
        email='joana@email.com',
        data_nascimento='1992-04-10',
        telefone=11911112222
    )
    cliente2 = Cliente.objects.create(
        usuario=user2,
        nome = 'Carlos',
        sobrenome='Ferreira',
        cpf='33333333333',
        email='carlos@email.com',
        data_nascimento='1988-12-25',
        telefone=11933334444
    )

    # Categorias
    categoria_notebook = Categoria.objects.create(categoria="Notebook")
    categoria_tv = Categoria.objects.create(categoria="TV")
    categoria_fone = Categoria.objects.create(categoria="Fone de Ouvido")

    # Produtos
    Produto.objects.create(
        produto="Notebook Dell",
        descricao="Notebook com alto desempenho.",
        ano_fabricacao=2022,
        nome_categoria=categoria_notebook,
        preco=4200.00,
        quantidade=5
    )
    Produto.objects.create(
        produto="Smart TV 50\"",
        descricao="TV com resolução 4K e apps integrados.",
        ano_fabricacao=2023,
        nome_categoria=categoria_tv,
        preco=3000.00,
        quantidade=3
    )
    Produto.objects.create(
        produto="Fone Bluetooth JBL",
        descricao="Fone sem fio com cancelamento de ruído.",
        ano_fabricacao=2021,
        nome_categoria=categoria_fone,
        preco=399.90,
        quantidade=10
    )

    # Interesses
    Interesse.objects.create(cliente=cliente1, interesse="Notebook")
    Interesse.objects.create(cliente=cliente1, interesse="Smart TV")
    Interesse.objects.create(cliente=cliente2, interesse="Fone de Ouvido")
    Interesse.objects.create(cliente=cliente2, interesse="Tablet")

    print("Banco de dados populado com sucesso!")

if __name__ == '__main__':
    popular_banco()
    # Para executar este script, use o seguinte comando no terminal: python populate.py
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

    # Interesses
    Interesse.objects.create(cliente=cliente1, interesse="Notebook")
    Interesse.objects.create(cliente=cliente1, interesse="Smart TV")
    Interesse.objects.create(cliente=cliente2, interesse="Fone de Ouvido")
    Interesse.objects.create(cliente=cliente2, interesse="Tablet")

    categorias = [
        Categoria.objects.create(categoria="Notebook"),
        Categoria.objects.create(categoria="TV"),
        Categoria.objects.create(categoria="Fone de Ouvido"),
        Categoria.objects.create(categoria="Tablet"),
        Categoria.objects.create(categoria="Monitor"),
    ]

    nomes_produtos = [
        ("Notebook Dell", "Notebook com alto desempenho."),
        ("Smart TV 50\"", "TV com resolução 4K."),
        ("Fone JBL", "Fone com cancelamento de ruído."),
        ("Tablet Samsung", "Tablet Android com boa bateria."),
        ("Monitor LG", "Monitor ultrawide."),
        ("Notebook Acer", "Notebook com bom custo-benefício."),
        ("TV LG 43\"", "TV Full HD com SmartOS."),
        ("Fone Sony", "Fone Bluetooth com microfone."),
        ("Tablet Lenovo", "Tablet ideal para estudo."),
        ("Monitor Samsung", "Monitor 24\" Full HD."),
        ("Notebook Apple", "MacBook Air M2."),
        ("Smart TV Samsung 60\"", "TV 4K HDR."),
        ("Fone Xiaomi", "Fone de ouvido leve e confortável."),
        ("Notebook Positivo", "Modelo básico para tarefas simples."),
        ("Monitor Dell", "Monitor com excelente contraste."),
        ("Tablet Amazon Fire", "Ideal para leitura."),
        ("Fone Philips", "Modelo com fio."),
        ("Notebook HP", "Com tela antirreflexo."),
        ("TV Philco", "Smart TV custo-benefício."),
        ("Tablet Multilaser", "Modelo infantil.")
    ]

    for nome, desc in nomes_produtos:
        categoria = choice(categorias)
        Produto.objects.create(
            produto=nome,
            descricao=desc,
            ano_fabricacao=randint(2018, 2023),
            nome_categoria=categoria,
            preco=Decimal(randint(500, 6000)),
            quantidade=randint(1, 10),
            status=choice(['D', 'V', 'R']),
            autor_modificacao=Usuario.objects.filter(is_superuser=True).first()
        )

    print("Banco de dados populado com sucesso!")

if __name__ == '__main__':
    popular_banco()
    # Para executar este script, use o seguinte comando no terminal: python populate.py
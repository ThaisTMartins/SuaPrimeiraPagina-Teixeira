from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Usuario, Cliente
from django.http import HttpResponse
from .forms import ClienteForm, InteresseForm, ProdutoForm, PesquisaProdutoForm

def index(request):
    return HttpResponse("Olá, bem vindo ao APP!")

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'App/lista_usuario.html', {'usuarios': usuarios})

def detalhe_usuarios(request, usuario_id): #informações do cliente
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    cliente = Cliente.objects.filter(usuario=usuario).first()  # Obtém o cliente associado ao usuário, se existir
    return render(request, 'App/detalhe_usuario.html', {'cliente': cliente, 'usuario': usuario})

def lista_produtos_disponiveis(request):
    form = PesquisaProdutoForm(request.GET)  # Cria o formulário de pesquisa
    if form.is_valid():
        termo = form.cleaned_data.get('termo')
        if termo:
            produtos_disponiveis = Produto.objects.filter(
                produto__icontains=termo
            )
        else:
            produtos_disponiveis = Produto.objects.all()
    else:
        produtos_disponiveis = Produto.objects.all()
    return render (request, 'App/lista_produtos_disponiveis.html', {'produtos': produtos_disponiveis, 'form': form})

def criar_clientes(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)  # Garante que o usuário existe

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = usuario  # Associa o cliente ao usuario (OneToOne)
            cliente.save()
            return redirect('detalhe_usuarios', usuario_id=usuario_id)  # Redireciona para a página de detalhes do usuário, após salvar o cliente

    else:
        form = ClienteForm()

    return render(request, 'App/criar_cliente.html', {'form': form, 'usuario': usuario})  # Garante um retorno sempre

def criar_interesse(request, usuario_id, cliente_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)  # Garante que o usuário existe
    cliente = get_object_or_404(Cliente, pk=cliente_id)  # Garante que o cliente existe

    if request.method == 'POST':
        form = InteresseForm(request.POST)
        if form.is_valid():
            interesse = form.save(commit=False)
            interesse.cliente = cliente
            interesse.save()
            return redirect('detalhe_usuarios', usuario_id=usuario_id)  # Redireciona para a página de detalhes do usuário, após salvar o interesse
    else:
        form = InteresseForm()
    return render(request, 'App/criar_interesse.html', {'form': form, 'usuario': usuario, 'cliente': cliente})  # Garante um retorno sempre

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos_disponiveis')  # Redireciona para a lista de produtos disponíveis após salvar
    else:
        form = ProdutoForm()
    return render(request, 'App/criar_produto.html', {'form': form})  # Garante um retorno sempre

# def pesquisa_produto(request):
#     resultados = None
#     form = PesquisaProdutoForm(request.GET)  


#     if form.is_valid():
#         termo = form.cleaned_data.get('termo')
#         if termo:
#             resultados = Produto.objects.filter(
#                 produto__icontains=termo
#             )

#     return render(request, 'App/pesquisa_produto.html', {'form': form, 'resultados': resultados})

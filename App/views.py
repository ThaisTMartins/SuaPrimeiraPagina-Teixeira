from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Usuario, Cliente
from django.http import HttpResponse
from .forms import ClienteForm

def index(request):
    return HttpResponse("Olá, bem vindo ao APP!")

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'App/lista_usuario.html', {'usuarios': usuarios})

def detalhe_usuarios(request, pk): #informações do cliente
    cliente = get_object_or_404(Usuario, pk=pk)
    return render(request, 'App/detalhe_usuario.html', {'cliente': cliente})

def lista_produtos_disponiveis(request):
    produtos_disponiveis = Produto.objects.all()
    return render (request, 'App/lista_produtos_disponiveis.html', {'produtos': produtos_disponiveis})

def criar_clientes(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)  # Garante que o usuário existe

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = usuario  # Associa o cliente ao usuario (OneToOne)
            cliente.save()
            return redirect('detalhe_usuarios', pk=pk)  # Redireciona para a página de detalhes do usuário, após salvar o cliente

    else:
        form = ClienteForm()

    return render(request, 'App/criar_cliente.html', {'form': form, 'usuario': usuario})  # Garante um retorno sempre
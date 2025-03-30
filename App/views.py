from django.shortcuts import render, get_object_or_404
from .models import Produto, Usuario, Cliente
from django.http import HttpResponse

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
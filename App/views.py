from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Usuario, Cliente, Avatar, Categoria
from django.http import HttpResponse
from .forms import ClienteForm, InteresseForm, ProdutoForm, PesquisaProdutoForm, UsuarioForm, CategoriaForm, AvatarForm, UsuarioUpdateForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

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

@login_required
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos_disponiveis')  # Redireciona para a lista de produtos disponíveis após salvar
    else:
        form = ProdutoForm()
    return render(request, 'App/criar_produto.html', {'form': form})  # Garante um retorno sempre

@login_required
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuario')  # Redireciona para a lista de produtos disponíveis após salvar
    else:
        form = UsuarioForm()
    return render(request, 'App/criar_usuario.html', {'form': form})  # Garante um retorno sempre

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')  # Redireciona para a lista de categorias após salvar
    else:
        form = CategoriaForm()
    return render(request, 'App/criar_categoria.html', {'form': form})  # Garante um retorno sempre

@login_required
def lista_categorias(request):
    categoria = Categoria.objects.all()
    return render(request, 'App/lista_categorias.html', {'categoria': categoria})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        user_form = UsuarioUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, request.user)  # Mantém o usuário logado após alteração de senha
            messages.success(request, "Perfil e senha atualizados com sucesso!")
            return redirect('perfil')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        user_form = UsuarioUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'App/editar_perfil.html', {
        'user_form': user_form,
        'password_form': password_form
    })


@login_required
def upload_avatar(request):
    avatar, created = Avatar.objects.get_or_create(user=request.user)  # Tenta obter ou cria um novo avatar

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redireciona para o perfil
    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'App/upload_avatar.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'App/perfil.html', {'user': request.user})

def sobre(request):
    return render(request, 'App/sobre.html')

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto.save()
            return redirect('lista_produtos_disponiveis')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'App/editar_produto.html', {'form': form})
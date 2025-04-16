from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Usuario, Cliente, Avatar, Categoria, Interesse
from django.http import HttpResponse
from .forms import (ClienteForm, InteresseForm, ProdutoForm, PesquisaProdutoForm, RegistroUsuarioForm, UsuarioForm,
                    CategoriaForm, AvatarForm, UsuarioUpdateForm, CustomPasswordChangeForm, AdminSetPasswordForm)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseForbidden
from django.utils import timezone

# Outras views
def index(request):
    return HttpResponse("Olá, bem vindo ao APP!")

@login_required
def perfil(request):
    return render(request, 'App/perfil.html', {'user': request.user})

def sobre(request):
    return render(request, 'App/sobre.html')

# Visualizar
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'App/lista_usuario.html', {'usuarios': usuarios})

@login_required
def detalhe_usuarios(request, usuario_id): #informações do cliente
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    cliente = Cliente.objects.filter(usuario=usuario).first()  # Obtém o cliente associado ao usuário, se existir
    return render(request, 'App/detalhe_usuario.html', {'cliente': cliente, 'usuario': usuario})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'App/detalhe_produto.html', {'produto': produto})

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

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'App/lista_categorias.html', {'categorias': categorias})

# Inserir
@login_required
def criar_clientes(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)  # Garante que o usuário existe

    if request.user.pk != usuario_id:
        return HttpResponseForbidden("Você não tem permissão para editar este cliente.")

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

@login_required
def criar_interesse(request, usuario_id, cliente_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)  # Garante que o usuário existe
    cliente = get_object_or_404(Cliente, pk=cliente_id)  # Garante que o cliente existe

    if request.user.pk != usuario_id:
        return HttpResponseForbidden("Você não tem permissão para editar este cliente.")

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
            produto = form.save(commit=False)
            produto.data_publicacao = timezone.now()  # Adiciona a data de publicação automaticamente
            produto.data_modificao = timezone.now()
            produto.autor_modificacao = request.user  # Associa o produto ao usuário logado no momento
            form.save()
            return redirect('lista_produtos_disponiveis')  # Redireciona para a lista de produtos disponíveis após salvar
    else:
        form = ProdutoForm()
    return render(request, 'App/criar_produto.html', {'form': form})

def criar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            # Verifica se o nome de usuário já existe
            if Usuario.objects.filter(username=username).exists():
                # Se o usuário já existir, mostramos uma mensagem de erro
                messages.error(request, "Este nome de usuário já está em uso. Tente outro.")
                return redirect('criar_usuario')  # Redireciona de volta para a tela de registro

            # Salvando o novo usuário
            usuario = form.save(commit=False)
            usuario.tipo_usuario = Usuario.TipoUsuario.cliente  # Define o tipo de usuário como cliente por padrão
            usuario.set_password(form.cleaned_data['password'])  # Definindo a senha de maneira segura
            usuario.save()

            # Autenticando o usuário automaticamente após o registro
            login(request, usuario)

            # Mensagem de sucesso
            messages.success(request, "Cadastro realizado com sucesso! Você foi autenticado.")

            # Redirecionando para a página inicial ou outra página de sucesso
            return redirect('home')  # Altere 'home' para o nome de URL da sua página inicial
        else:
            print(form.errors)
    else:
        form = RegistroUsuarioForm()

    return render(request, 'App/criar_usuario.html', {'form': form})

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

# Editar
@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.data_modificao = timezone.now()
            produto.data_publicacao = produto.data_publicacao  # Mantém a data de publicação original
            produto.autor_modificacao = request.user  # Associa o produto ao usuário logado no momento
            produto.save()
            return redirect('lista_produtos_disponiveis')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'App/editar_produto.html', {'form': form})

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'App/editar_categoria.html', {'form': form})

@login_required
def editar_cliente(request, usuario_id, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id, usuario_id=usuario_id)

    if request.user.pk != usuario_id:
        return HttpResponseForbidden("Você não tem permissão para editar este cliente.")
    
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente.save()
            return redirect('detalhe_usuarios', usuario_id=usuario_id)
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'App/editar_cliente.html', {'form': form, 'usuario_id': usuario_id, 'cliente_id': cliente_id})

@login_required
def editar_interesse(request, usuario_id, cliente_id, interesse_id):
    interesse = get_object_or_404(Interesse, id=interesse_id)

    if request.user.pk != usuario_id:
        return HttpResponseForbidden("Você não tem permissão para editar este cliente.")
    
    if request.method == "POST":
        form = InteresseForm(request.POST, instance=interesse)
        if form.is_valid():
            interesse.save()
            return redirect('detalhe_usuarios', usuario_id=usuario_id)
    else:
        form = InteresseForm(instance=interesse)

    return render(request, 'App/editar_interesse.html', {'form': form, 'usuario_id': usuario_id, 'cliente_id': cliente_id})
    
@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    is_admin = request.user.is_superuser
    is_self = usuario == request.user

    if request.method == 'POST':
        user_form = UsuarioUpdateForm(request.POST, instance=usuario, is_admin = is_admin)
        
        if is_admin and not is_self:
            # Se o usuário for admin, pode alterar a senha de outro usuário
            password_form = AdminSetPasswordForm(user=usuario, data=request.POST)
        elif is_self:
            # Se o usuário for ele mesmo, pode alterar a própria senha
            password_form = PasswordChangeForm(user=usuario, data=request.POST)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar este usuário.")
        
        if user_form.is_valid() and password_form.is_valid():
            # Atualiza o usuário com os dados do formulário (nome de usuário)
            user_form.save()
            password_form.save()

            if is_self:
                update_session_auth_hash(request, password_form.user)  # Mantém o usuário logado após alteração de senha
                print("Senha alterada com sucesso!")
            
            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('home')            
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        user_form = UsuarioUpdateForm(instance=usuario, initial={'is_admin': is_admin})
        
        if is_admin and not is_self:
            # Se o usuário for admin, pode alterar a senha de outro usuário
            password_form = AdminSetPasswordForm(user=usuario, data=request.POST)
        elif is_self:
            # Se o usuário for ele mesmo, pode alterar a própria senha
            password_form = PasswordChangeForm(user=usuario, data=request.POST)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar este usuário.")

    return render(request, 'App/editar_usuario.html', {
        'user_form': user_form,
        'password_form': password_form,
    })  

# Upload
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

# Deletar
@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
   
    if request.method == "POST":
        produto.delete()
        return redirect('lista_produtos_disponiveis')

    return render(request, 'App/confirmar_deletar_produto.html', {'produto': produto})

@login_required
def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
   
    if request.method == "POST":
        usuario.delete()
        return redirect('lista_usuarios')

    return render(request, 'App/confirmar_deletar_usuario.html', {'usuario': usuario})

@login_required
def deletar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
   
    if request.method == "POST":
        categoria.delete()
        return redirect('lista_categorias')

    return render(request, 'App/confirmar_deletar_categoria.html', {'categoria': categoria})

@login_required
def deletar_interesse(request, usuario_id, cliente_id, interesse_id):
    interesse = get_object_or_404(Interesse, id=interesse_id)

    if request.user.pk != usuario_id:
        return HttpResponseForbidden("Você não tem permissão para editar este cliente.")
   
    if request.method == "POST":
        interesse.delete()
        return redirect('detalhe_usuarios', usuario_id=usuario_id)

    return render(request, 'App/confirmar_deletar_interesse.html', {'interesse': interesse, 'usuario_id': usuario_id, 'cliente_id': cliente_id})
from django.urls import path, include
from .views import lista_usuarios, lista_produtos_disponiveis, detalhe_usuarios, criar_clientes, criar_interesse, criar_produto, criar_usuario, upload_avatar, sobre, perfil, editar_perfil, criar_categoria, lista_categorias, editar_produto
from django.contrib.auth import views as auth_views  

urlpatterns = [
    path('usuarios/', lista_usuarios, name = 'lista_usuarios'),
    path('usuarios/<int:usuario_id>/detalhe_usuario', detalhe_usuarios, name = 'detalhe_usuarios'),
    path('usuarios/<int:usuario_id>/clientes/<int:pk>/', detalhe_usuarios, name = 'detalhe_usuarios'),
    path('produtos', lista_produtos_disponiveis, name = 'lista_produtos_disponiveis'),
    path('usuarios/<int:usuario_id>/criar_cliente', criar_clientes, name = 'criar_cliente'),
    path('usuarios/<int:usuario_id>/clientes/<int:cliente_id>/criar_interesse', criar_interesse, name='criar_interesse'),
    path('criar_produto', criar_produto, name='criar_produto'),
    path('criar_usuario', criar_usuario, name= 'criar_usuario'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('editar-avatar/', upload_avatar, name='editar_avatar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', sobre, name='sobre'),
    path('criar_categoria', criar_categoria, name='criar_categoria'),
    path('lista_categorias', lista_categorias, name='lista_categorias'),
    path('deletar_categoria/<int:categoria_id>/', lista_categorias, name='deletar_categoria'),
    path('deletar_usuario/<int:usuario_id>/', lista_usuarios, name='deletar_usuario'),
    path('deletar_cliente/<int:cliente_id>/', detalhe_usuarios, name='deletar_cliente'),
    path('deletar_produto/<int:produto_id>/', lista_produtos_disponiveis, name='deletar_produto'),
    path('deletar_interesse/<int:interesse_id>/', detalhe_usuarios, name='deletar_interesse'),
    path('deletar_avatar/<int:avatar_id>/', perfil, name='deletar_avatar'),
    path('editar_categoria/<int:categoria_id>/', lista_categorias, name='editar_categoria'),
    path('editar_usuario/<int:usuario_id>/', lista_usuarios, name='editar_usuario'),
    path('editar_cliente/<int:cliente_id>/', detalhe_usuarios, name='editar_cliente'),
    path('editar_produto/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('editar_interesse/<int:interesse_id>/', detalhe_usuarios, name='editar_interesse'),
    path('editar_avatar/<int:avatar_id>/', perfil, name='editar_avatar'),
]
from django.urls import path, include
from .views import lista_usuarios, lista_produtos_disponiveis, detalhe_usuarios, criar_clientes, criar_interesse, criar_produto, criar_usuario, upload_avatar, sobre, perfil, editar_perfil#, pesquisa_produto
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
    # path('pesquisa_produto', pesquisa_produto, name='pesquisa_produto'),
    path('perfil/', perfil, name='perfil'),

    path('editar-avatar/', upload_avatar, name='editar_avatar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', sobre, name='sobre'),
]
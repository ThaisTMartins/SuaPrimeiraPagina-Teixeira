from django.urls import path, include
from .views import lista_usuarios, lista_produtos_disponiveis, detalhe_usuarios, criar_clientes, criar_interesse, criar_produto, criar_usuario, upload_avatar#, pesquisa_produto

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
    path('editar-avatar/', upload_avatar, name='editar_avatar'),
]
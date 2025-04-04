from django.urls import path, include
from .views import lista_usuarios, lista_produtos_disponiveis, detalhe_usuarios, criar_clientes

urlpatterns = [
    path('usuarios/', lista_usuarios, name = 'lista_usuarios'),
    path('usuarios/pk=usuario.pk/detalhe_usuario', detalhe_usuarios, name = 'detalhe_usuarios'),
    path('clientes/<int:pk>/', detalhe_usuarios, name = 'detalhe_usuarios'),
    path('produtos', lista_produtos_disponiveis, name = 'lista_produtos_disponiveis'),
    path('clientes/<int:pk>/criar_cliente', criar_clientes, name = 'criar_cliente'),
]
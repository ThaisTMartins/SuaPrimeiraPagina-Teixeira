from django.urls import path, include
from .views import lista_usuarios, lista_produtos_disponiveis, detalhe_usuarios

urlpatterns = [
    path('usuarios/', lista_usuarios, name = 'lista_usuario'),
    path('clientes/<int:pk>/', detalhe_usuarios, name = 'detalhe_usuario'),
    path('produtos', lista_produtos_disponiveis, name = 'lista_produtos_disponiveis'),
]
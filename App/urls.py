from django.urls import path, include
from .views import (lista_usuarios, lista_categorias, detalhe_usuarios,
                    criar_clientes, criar_interesse, criar_usuario, criar_categoria,
                    upload_avatar, sobre, perfil, editar_categoria, editar_interesse, editar_cliente, editar_usuario,
                    deletar_categoria, deletar_interesse, deletar_usuario)
from .views import produto_list_view, produto_create_view, produto_update_view, produto_delete_view, produto_detail_view
from django.contrib.auth import views as auth_views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('usuarios/', lista_usuarios, name = 'lista_usuarios'),
    path('usuarios/<int:usuario_id>/editar_usuario', editar_usuario, name = 'editar_usuario'),
    path('usuarios/<int:usuario_id>/deletar_usuario', deletar_usuario, name = 'deletar_usuario'),
    path('usuarios/<int:usuario_id>/detalhe_usuario/', detalhe_usuarios, name='detalhe_usuarios'),
    path('usuarios/<int:usuario_id>/criar_cliente', criar_clientes, name = 'criar_cliente'),
    path('usuarios/<int:usuario_id>/clientes/<int:cliente_id>/criar_interesse', criar_interesse, name='criar_interesse'),
    path('usuarios/<int:usuario_id>/clientes/<int:cliente_id>/editar_interesse/<int:interesse_id>/', editar_interesse, name='editar_interesse'),
    path('usuarios/<int:usuario_id>/clientes/<int:cliente_id>/deletar_interesse/<int:interesse_id>/', deletar_interesse, name='deletar_interesse'),
    path('usuarios/<int:usuario_id>/editar_cliente/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('criar_usuario', criar_usuario, name= 'criar_usuario'),
    path('criar_categoria', criar_categoria, name='criar_categoria'),
    path('lista_categorias', lista_categorias, name='lista_categorias'),
    path('categorias/<int:categoria_id>/deletar_categoria/', deletar_categoria, name='deletar_categoria'),
    path('editar_categoria/<int:categoria_id>/', editar_categoria, name='editar_categoria'),
    path('editar-avatar/', upload_avatar, name='editar_avatar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', sobre, name='sobre'),
    path('deletar_avatar/<int:avatar_id>/', perfil, name='deletar_avatar'),
    path('editar_avatar/<int:avatar_id>/', perfil, name='editar_avatar'),
    path('produtos/', produto_list_view.as_view(), name='lista_produtos_disponiveis'),
    path('criar_produto', produto_create_view.as_view(), name='criar_produto'),
    path('editar_produto/<int:produto_id>/', produto_update_view.as_view(), name='editar_produto'),
    path('produtos/<int:produto_id>/deletar_produto/', produto_delete_view.as_view(), name='deletar_produto'),
    path('produtos/<int:produto_id>/detalhe_produto/', produto_detail_view.as_view(), name='detalhe_produto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
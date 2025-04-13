from django.contrib import admin
from .models import Usuario, Produto, Categoria, Cliente, Interesse

admin.site.register(Usuario)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Interesse)

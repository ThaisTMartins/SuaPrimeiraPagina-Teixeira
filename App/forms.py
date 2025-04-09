from django import forms
from .models import Cliente, Interesse, Produto, Usuario, Avatar, Categoria
from django.contrib.auth.forms import PasswordChangeForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['email', 'telefone', 'ano_nascimento', 'cpf']

class InteresseForm(forms.ModelForm):
    class Meta:
        model = Interesse
        fields = ['interesse']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto', 'descricao', 'ano_fabricacao', 'nome_categoria']

class PesquisaProdutoForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar Produto",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'})
    )

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'senha']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']  

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagem']

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome']  

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Usuario
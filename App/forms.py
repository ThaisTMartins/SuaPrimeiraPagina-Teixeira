from django import forms
from .models import Cliente, Interesse, Produto, Usuario, Avatar, Categoria
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class InteresseForm(forms.ModelForm):
    class Meta:
        model = Interesse
        fields = ['interesse']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto', 'descricao', 'ano_fabricacao', 'nome_categoria', 'preco', 'quantidade', 'status']

class PesquisaProdutoForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar Produto",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'})
    )

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=False, label='Confirmar Senha')

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'tipo_usuario']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('A senha deve ter pelo menos 8 caracteres.')
        if not any(char.isdigit() for char in password):
            raise ValidationError('A senha deve conter pelo menos um número.')
        if not any(char.isupper() for char in password):
            raise ValidationError('A senha deve conter pelo menos uma letra maiúscula.')
        return password


    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')


        if password != password_confirm:
            raise ValidationError('As senhas não coincidem.')
        return password_confirm

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
        fields = ['username', 'tipo_usuario']  

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Usuario
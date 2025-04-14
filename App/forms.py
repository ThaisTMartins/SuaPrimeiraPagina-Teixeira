from django import forms
from .models import Cliente, Interesse, Produto, Usuario, Avatar, Categoria
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }

    # Para no editar perfil garantir que importou o form-control e deixar a formatação igual ao de criar usuário
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'tipo_usuario']

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirmar Senha')

    class Meta:
        model = Usuario
        fields = ['username', 'password']
        # Não considero tipo_usuario, pois ele já é definido no models com o valor padrão de cliente, também forço o valor em views.py
        labels = {
            'username': 'Nome',
            'password': 'Senha',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise ValidationError('Esse nome de usuário já existe.')
        return username
    
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
        labels = {
            'username': 'Usuário',
        }

    def __init__(self, *args, **kwargs):
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs) 

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        if not is_admin:
            self.fields['tipo_usuario'].widget = forms.HiddenInput()

# Classe já é definida no Django, mas como não tem o label e o widget que eu quero, criei uma classe personalizada que sobrescreve a já existente
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha Atual",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label="Confirme a Nova Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
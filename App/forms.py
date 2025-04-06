from django import forms
from .models import Cliente, Interesse, Produto

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
        fields = ['produto', 'quantidade']

class PesquisaProdutoForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar Produto",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'})
    )

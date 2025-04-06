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
        fields = ['produto']
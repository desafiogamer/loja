from django import forms
from .models import Anuncio, AnuncioMoto

class CarroForms(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ["carro", "modelo", "descricao", "preco", "data", "km","cidade", "marca", "condicao", "precoo", "troca", "combustivel", "cambio", "cor", "ipva"]
    
    


class MotoForms(forms.ModelForm):
    class Meta:
        model = AnuncioMoto
        fields = ["moto", "modelo", "descricao", "preco", "data", "km","cidade", "marca", "condicao", "precoo", "troca", "Refrigeracao", "Partida", "cor", "ipva", "Cilindrada", "marchas"]

        
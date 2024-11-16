from django import forms
from ..models import Fabricante,Carro

class FormFabricante(forms.ModelForm):
    identif = forms.CharField(max_length=10,
                              label='Identificador',
                              widget=forms.TextInput(
                                  attrs={'class':'form-control'}
                              ))
    nombre = forms.CharField(max_length=100,
                             label='Nombre',
                             widget=forms.TextInput(
                                 attrs={'class':'form-control'}
                             ))
    
    class Meta:
        model = Fabricante
        fields = ['identif','nombre']


class FormCarro(forms.ModelForm):
    fabricante = forms.ModelChoiceField(
        queryset=Fabricante.objects.all(),
        label='Fabricante',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    modelo = forms.CharField(max_length=100, label='Modelo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    placa = forms.CharField(max_length=10, label='Placa', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Carro
        fields = ['modelo', 'fabricante', 'placa']
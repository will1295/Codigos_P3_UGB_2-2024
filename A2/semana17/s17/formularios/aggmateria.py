from django import forms

class FormMateria(forms.Form):
    cod = forms.CharField(max_length=10,
                          label='Código')
    nom = forms.CharField(max_length=150,
                          label='Nombre')
  

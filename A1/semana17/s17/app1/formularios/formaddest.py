from django import forms

class FormEst(forms.Form):
    nom = forms.CharField(max_length=100
                          ,label="Nombre")
    car = forms.CharField(max_length=10
                          ,label="Carnet")
    ed = forms.IntegerField(label="Edad")
    cur = forms.CharField(max_length=200
                          ,label="Curso")
  
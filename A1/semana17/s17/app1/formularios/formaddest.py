from django import forms
from ..models import Materias,Estudiantes

class FormEst(forms.ModelForm):
    nom = forms.CharField(max_length=100
                          ,label="Nombre")
    car = forms.CharField(max_length=10
                          ,label="Carnet")
    ed = forms.IntegerField(label="Edad")
    cur = forms.CharField(max_length=200
                          ,label="Curso")
    
    class Meta:
        model = Estudiantes
        fields = ['nombre','carnet','edad','curso']


class FormMaterias(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    estds = forms.ModelMultipleChoiceField(
        queryset=Estudiantes.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Materias
        fields = ['nombre', 'estds'] 

    
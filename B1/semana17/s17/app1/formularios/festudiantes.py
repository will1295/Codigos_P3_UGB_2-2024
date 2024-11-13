from django import forms
from ..models import Estudiante 
class AgregarEst(forms.ModelForm):  
    class Meta:
        model = Estudiante
        fields = ['nombre', 'codigo', 'edad', 'carrera', 'fingr']  # Asegúrate de que estos campos estén en el modelo Estudiante

    nom = forms.CharField(max_length=100,
                          label="Nombre",
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    cod = forms.CharField(max_length=10,
                          label="Código",
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    edad = forms.IntegerField(label="Edad",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))  # Cambié TextInput a NumberInput
    
    carr = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                           label="Carrera")
    
    fecha = forms.DateField(label="Año de ingreso",
                            widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

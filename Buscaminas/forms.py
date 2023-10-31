from django import forms
from django.core.exceptions import ValidationError

class CreaTableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas',min_value=1, max_value=20, required= True, initial=2)
    columnas = forms.IntegerField(label='Columnas', min_value=1, max_value=15, required=True, initial=2)
    nMinas = forms.IntegerField(label='Minas', min_value=1, required=True, initial=2)

def validar(self):
    cleaned_data=super().clean()
    filas = cleaned_data.get("filas")
    columnas = cleaned_data.get("columnas")
    nMinas= cleaned_data.get("minas") 

    if nMinas>((columnas*filas)/2):
        
        raise ValidationError(" Valor de minas no válido ")

    return cleaned_data








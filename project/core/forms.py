from django import forms
from . import models
from cliente.models import Reparacion,Cliente

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = models.Reparacion
        fields="__all__"

class BusquedaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Buscar')

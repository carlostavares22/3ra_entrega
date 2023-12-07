from django import forms
from . import models
from cliente.models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = models.Servicio
        fields="__all__"
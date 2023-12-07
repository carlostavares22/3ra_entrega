from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ReparacionForm,BusquedaForm
from cliente.models import Cliente, Reparacion
from django import forms

def home(request):
    if request.method == "POST":
        form = ReparacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = ReparacionForm()
    return render(request, "core/index.html", {"form": form})

def buscar_cliente(request):
    form = BusquedaForm(request.GET)
    resultados = None
    
    if request.method == 'GET' and 'nombre' in request.GET:
        form = BusquedaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Cliente.objects.filter(nombre__icontains=nombre)
    
    return render(request, 'core/buscar.html', {'form': form, 'resultados': resultados})
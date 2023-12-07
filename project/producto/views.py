from django.shortcuts import render, redirect
from .forms import ServicioForm
from cliente.models import Servicio

def crear(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = ServicioForm()
    return render(request, "producto/index.html", {"form": form})

from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def crear(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = ClienteForm()
    return render(request, "cliente/index.html", {"form": form})
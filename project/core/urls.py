from django.contrib import admin
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="index"),
    path("search/", views.buscar_cliente, name="search"),
]

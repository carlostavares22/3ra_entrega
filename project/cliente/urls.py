from django.contrib import admin
from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.crear, name="index"),
]
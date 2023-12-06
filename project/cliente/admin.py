from django.contrib import admin
from . import models

admin.site.register(models.Servicio)
admin.site.register(models.Cliente)
admin.site.register(models.Reparacion)
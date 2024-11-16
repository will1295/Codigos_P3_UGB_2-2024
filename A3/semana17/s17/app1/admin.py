from django.contrib import admin
from . import models

admin.site.register(models.Fabricante)

@admin.register(models.Carro)
class CarroAdmin(admin.ModelAdmin):
    pass


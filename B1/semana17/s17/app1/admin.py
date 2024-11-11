from django.contrib import admin
from . import models

admin.site.register(models.Estudiante)
"""
@admin.register(models.Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    pass
"""    
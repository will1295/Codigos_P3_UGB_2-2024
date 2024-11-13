from django.contrib import admin
from . import models

admin.site.register(models.Estudiantes)
admin.site.register(models.Materias)
"""
@admin.register(models.Estudiantes)
class EstAdmin(admin.ModelAdmin):
    pass
"""    
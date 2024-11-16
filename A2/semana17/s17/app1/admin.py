from django.contrib import admin
from .models import Materia,Estudiante

admin.site.register(Materia)

@admin.register(Estudiante)
class EstAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Tarea, Proyecto
# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
        list_display=(
            'nombre',
            'fecha',
            'propietario',
            'integrantes'
        )
        search_fields =(
            'nombre',
            'propietario'
        )    
        list_filter =(
            'propietario'
            
        )
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
        list_display=(
            'nombre',
            'fecha',
            'propietario',
            'proyecto',
            'estado',
            'asignado_a'

        )
        search_fields =(
            'nombre',
            'asignado_a',
            'proyecto'

        )    
        list_filter =(
            'propietario',
            'estado'
            
        )

#contraseña admin es palta
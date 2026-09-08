from django.contrib import admin
from .models import Tarea, Proyecto
# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
        list_display=(
            'nombre',
            'fecha_limite',
            'propietario',
            'integrantes_totales'
        )
        search_fields =(
            'nombre',
            'propietario'
        )    
        list_filter =(
            'propietario',
            
        )
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
        list_display=(
            'nombre',
            'fecha',
            'asignado_a',
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
            'asignado_a',
            'estado'
            
        )

#contraseña admin es palta
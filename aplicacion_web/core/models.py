from django.db import models
from django.conf import settings

# Create your models here.
#debo cambiar esto para asociar los modelos entre si
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    es_proyecto_completado = models.BooleanField(default=False)
    integrantes_totales = models.IntegerField(default=1)
    privado = models.BooleanField(default=True)
    propietario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="proyectos",)
    fecha_limite = models.DateField()
    def __str__(self):
        return self.nombre
class Tarea(models.Model):
    ESTADOS = [
        ('pendiente','Pendiente'),
        ('en_progreso','En progreso'),
        ('completado','Completado')
    ]
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name="tareas"
    )
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='pendiente')
    asignado_a = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tareas_asignadas'
    )    #auto_now=False es para actualizar la fecha despues de cada modificacion
    #del objeto 
    def __str__(self):
        return self.nombre
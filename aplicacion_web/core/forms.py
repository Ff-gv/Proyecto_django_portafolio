from django import forms
from .models import Proyecto, Tarea
from datetime import date
class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'integrantes_totales', 'privado', 'fecha_limite']
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del proyecto",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descripción del proyecto",
                }
            ),
            "integrantes_totales": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1", 
                    "placeholder": "Cantidad de integrantes",
                }
            ),
            "privado": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
            "fecha_limite": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }
    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get("fecha_limite")
        if fecha_limite and fecha_limite < date.today():
            raise forms.ValidationError("La fecha no puede ser menor a la de hoy")
        return fecha_limite
    def clean_integrantes_totales(self):
        integrantes_totales = self.cleaned_data.get("integrantes_totales")
        if integrantes_totales and integrantes_totales <= 0:
            raise forms.ValidationError("Integrantes deben ser mayor a 0")
        return integrantes_totales
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre:
            sin_espacios = nombre.replace(" ", "") 
            if not sin_espacios.isalpha(): 
                raise forms.ValidationError("Nombre solo debe contener letras")
        return nombre

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre','descripcion','estado']
        widgets ={
        "nombre":forms.TextInput(attrs={"class":"form-control", "placeholder":"Nombre de la tarea"}),
        "descripcion": forms.Textarea(
                        attrs={
                            "class": "form-control",
                            "rows": 4,
                            "placeholder": "Descripción del proyecto",
                        }
                    ),
        "estado": forms.Select(attrs={"class": "form-select"})}
    def clean_nombre(self):
            nombre = self.cleaned_data.get("nombre")
            if nombre:
                sin_espacios = nombre.replace(" ", "") 
                if not sin_espacios.isalpha(): 
                    raise forms.ValidationError("Nombre solo debe contener letras")
            return nombre    
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from .forms import ProyectoForm, TareaForm
#claro, al final cada vista como clase que quiero llamar tiene que tener una 
#herencia? importada? de django, sirve para automatizar los procesos para cargar
#una pagina pero siempre tiene que ir el loginrequiredmixin para preguntar si es
#un usuario registrado
from .models import Proyecto, Tarea
# esto en conjunto muestra la pagina para un usuario registrado donde contiene la lista de los
#proyectos asociados a el.
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'core/dashboard.html'
    #se designa la variable template_name que representa la direccion de la pagina a utilizar
    #get_context prepara mis datos de la base de datos para ser enviado a la pagina dashboard
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)#aca se obtiene el get_context_data de
        #TemplateView, la clase ya hecha en django
        contexto["proyectos"] = Proyecto.objects.filter(propietario=self.request.user)
        return contexto
    #proyectos es un nombre ficticio nuevo que se crea y que se referenciara en html, el
    #proyecto.objects.filter viene de mi modelo y filtra segun el nombre del propietario del 
    #proyecto
    #esto crea un proyecto
class ProyectoCreateView(LoginRequiredMixin,CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "core/proyecto_form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        #esto lista solamente a peticion del usuario que envia la solicitud
        return super().form_valid(form)

class EsPropietarioProyectoMixin(UserPassesTestMixin):
    def test_func(self):
        proyecto = self.get_object()
        return proyecto.propietario == self.request.user
    #una verificacion, se suponde que compara el usuario logeado y activo que da la orden con
    #un usuario guardado dentro del modelo proyecto
class ProyectoUpdateView(LoginRequiredMixin,EsPropietarioProyectoMixin,UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    success_url = reverse_lazy("dashboard")
class ProyectoDeleteView(LoginRequiredMixin,EsPropietarioProyectoMixin,DeleteView):
    model = Proyecto
    template_name = "core/proyecto_delete.html"
    success_url = reverse_lazy("dashboard")
#con esto cubre todo lo que es crud de proyecto
class TareaListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model=Tarea
    template_name = "core/tarea_list.html"
    context_object_name = "tareas"
    def test_func(self):
        proyecto = get_object_or_404(
            Proyecto,
            pk=self.kwargs["proyecto_id"]
        )
        return proyecto.propietario == self.request.user
        #asegura de que la tarea pertenezca al proyecto, se coloca la funcion get object or 404
        #y se coloca el modelo proyecto donde se va a buscar, se coloca la clave con la que se
        #va a identificar el proyecto asociado con la tarea y si no existe salta error
        
    def get_queryset(self):
        return Tarea.objects.filter(
            proyecto_id=self.kwargs["proyecto_id"]
        )
    
    #esto llama a la tarea que solo coincida en su id de proyecto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyecto"] = get_object_or_404(
            Proyecto,
            pk=self.kwargs["proyecto_id"]
        )
        return context
    #crea diccionario y forma la lista
class TareaCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = "core/tarea_form.html"
    def test_func(self):
        proyecto = get_object_or_404(
            Proyecto,
            pk=self.kwargs["proyecto_id"]
        )
        return proyecto.propietario == self.request.user
    def form_valid(self, form):
        form.instance.proyecto_id = self.kwargs["proyecto_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "tarea_list",
            kwargs={"proyecto_id": self.kwargs["proyecto_id"]}
        )   


class TareaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "core/tarea_form.html"

    def test_func(self):
        tarea = self.get_object()
        return tarea.proyecto.propietario == self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "dashboard")


class TareaDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Tarea
    template_name = "core/tarea_delete.html"

    def test_func(self):
        tarea = self.get_object()
        return tarea.proyecto.propietario == self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "tarea_list",
            kwargs={"proyecto_id": self.object.proyecto_id}
        )
    
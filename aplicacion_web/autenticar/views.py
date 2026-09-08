from django.shortcuts import render
from .forms import RegistroForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.
def homeview(request):
    return render(request,'autenticar/home.html')
class LoginUserView(LoginView):
    template_name = "autenticar/login.html"
class LogoutUserView(LogoutView):
    next_page = reverse_lazy("login")

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = "autenticar/register.html"
    success_url = reverse_lazy("login")
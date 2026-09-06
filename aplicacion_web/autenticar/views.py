from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'autenticar/home.html')
def login_view(request):
    return render(request,'autenticar/login.html')
def register_view(request):
    return render(request,'autenticar/register.html')
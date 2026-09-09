from django.urls import path
from .views import *
urlpatterns = [
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('register/',RegistroView.as_view(),name='register')
]

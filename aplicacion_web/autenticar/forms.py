from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese su correo electronico'}))
    class Meta: 
        model=User
        fields=["username","email"]
    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if len(username) < 4:
            raise forms.ValidationError(
        "El nombre de usuario debe tener al menos 4 caracteres")
        return username
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ingrese nombre de usuario",
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ingrese su contraseña",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirme su contraseña",
        })    

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ingrese nombre de usuario",
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Ingrese su contraseña",
        })
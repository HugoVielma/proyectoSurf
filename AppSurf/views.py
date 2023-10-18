from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from tienda.views import tienda

def inicio(req):
    return render(req, "inicio.html")

def loginview(req):
    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
        else:
            return render(req, "inicio.html", {"mensaje": f"Datos incorrectos para login"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})

def register(req):
    if req.method == 'POST':
        miFormulario = UserCreationForm(data=req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con exito!"})
        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
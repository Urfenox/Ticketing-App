from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import RegistroForm

# Create your views here.

def home(respuesta):
    return render(respuesta, "main/home.html", {})

def signup(respuesta):
    form = RegistroForm(respuesta.POST or None)
    if respuesta.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/tickets")
    return render(respuesta, "registration/signup.html", {"form":form})

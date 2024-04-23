from django.shortcuts import render

# Create your views here.

def home(respuesta):
    return render(respuesta, "main/home.html", {})

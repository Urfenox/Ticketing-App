from django.shortcuts import render

# Create your views here.

def home(respuesta):
    return render(respuesta, "ticketing/home.html", {})

def create(respuesta):
    return render(respuesta, "ticketing/create.html", {})

def edit(respuesta, id):
    return render(respuesta, "ticketing/edit.html", {"id": id})

def delete(respuesta, id):
    return render(respuesta, "ticketing/delete.html", {"id": id})

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import TicketForm

# Create your views here.

def home(respuesta):
    return render(respuesta, "ticketing/home.html", {})

def create(respuesta):
    if respuesta.method == "POST":
        form = TicketForm(respuesta.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/tickets")
    else:
        form = TicketForm()
    return render(respuesta, "ticketing/create.html", {"form":form})

def edit(respuesta, id):
    return render(respuesta, "ticketing/edit.html", {"id": id})

def delete(respuesta, id):
    return render(respuesta, "ticketing/delete.html", {"id": id})

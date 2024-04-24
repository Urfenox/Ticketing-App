from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from .models import Ticket
from django.contrib import messages

# Create your views here.

def home(respuesta):
    tickets = Ticket.objects.all()
    return render(respuesta, "ticketing/home.html", {"tickets":tickets})

def create(respuesta):
    form = TicketForm()
    if respuesta.method == "POST":
        form = TicketForm(respuesta.POST)
        if form.is_valid():
            form.save()
            messages.success(respuesta, '¡Ticket creado correctamente!')
            return redirect("home")
        else:
            messages.error(respuesta, form.errors)
    return render(respuesta, "ticketing/create.html", {"form":form})

def edit(respuesta, id):
    ticket = get_object_or_404(Ticket, id=id) # pk=id o id=id funcionan | si no existe la ID, 404
    form = TicketForm(respuesta.POST or None, instance=ticket)
    if respuesta.method == "POST" and form.is_valid():
        form.save()
        messages.success(respuesta, '¡Ticket editado correctamente!')
        return redirect("home")
    else:
        messages.error(respuesta, form.errors)
    return render(respuesta, "ticketing/edit.html", {"ticket":ticket ,"form": form})

def delete(respuesta, id):
    messages.error(respuesta, "Esta funcion no se encuentra habilitada.")
    return redirect("home")
    # ticket = get_object_or_404(Ticket, id=id)
    # ticket.delete()
    # messages.success(respuesta, '¡Ticket eliminado correctamente!')
    # return redirect("home")

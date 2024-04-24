from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm, ComentarioForm
from .models import Ticket, Comentario
from django.contrib import messages
import os.path

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

def view(respuesta, id):
    ticket = get_object_or_404(Ticket, id=id)
    comentarios = Comentario.objects.filter(ticket_id=id).order_by('-publicacion')
    form = ComentarioForm(respuesta.POST or None, respuesta.FILES or None)
    if respuesta.method == "POST" and form.is_valid():
        archivo = respuesta.FILES.get('adjunto', None)
        nuevo = Comentario(ticket=ticket, usuario=form.cleaned_data['usuario'], mensaje=form.cleaned_data['mensaje'], adjunto=archivo)
        nuevo.save()
        messages.success(respuesta, '¡Comentario enviado!')
        return redirect(str("/tickets/view/{}".format(id)))
    else:
        messages.error(respuesta, form.errors)
    return render(respuesta, "ticketing/view.html", {"ticket":ticket, "form":form, "comentarios":comentarios})

def adjuntos(respuesta, uid):
    archivo = str("adjuntos/{}".format(uid))
    # verificar si el archivo existe
    if os.path.isfile(archivo):
        return FileResponse(
                open(archivo, "rb"),
                as_attachment=False,
                filename=uid # o obtener el nombre y formato del archivo
        )
    messages.error(respuesta, "Adjunto no encontrado.")
    return redirect("home")

from django.contrib import admin
from .models import Categoria, Ticket, Comentario
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Ticket)
admin.site.register(Comentario)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    NIVELES = {
        1: "NIVEL 1",
        2: "NIVEL 2",
        3: "NIVEL 3",
        4: "NIVEL 4"
    }
    nombre = models.CharField(max_length=100)
    nivel = models.SmallIntegerField(choices=NIVELES)

    def __str__(self):
        return self.nombre

class Ticket(models.Model):
    ESTADOS = {
        "O": "ABIERTO",
        "P": "PENDIENTE",
        "C": "COMPLETADO"
    }
    asunto = models.CharField(max_length=300)
    mensaje = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=ESTADOS, default="O")
    prioridad = models.PositiveSmallIntegerField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.asunto

class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    mensaje = models.TextField()
    adjunto = models.FileField(upload_to="comentarios", blank=True)

    def __str__(self):
        return self.mensaje[0:10]

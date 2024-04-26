from django import forms
from ticketing.models import Ticket, Comentario

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["asunto", "mensaje", "categoria", "prioridad"]
        widgets = {
            "asunto": forms.TextInput(attrs={"class": "form-control"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "prioridad": forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "5"}),
        }

class ComentarioForm(forms.Form):

    usuario = forms.CharField(required=True)
    mensaje = forms.CharField(required=True)
    adjunto = forms.FileField(required=False)

    usuario.widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de usuario"})
    mensaje.widget = forms.Textarea(attrs={"class": "form-control", "rows":"3", "placeholder": ""})
    adjunto.widget = forms.FileInput(attrs={"class": "form-control", "placeholder": "Opcional"})

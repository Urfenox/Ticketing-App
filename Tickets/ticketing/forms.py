from django import forms
from ticketing.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["asunto", "mensaje", "categoria", "prioridad"]
        widgets = {
            "asunto": forms.TextInput(attrs={"class": "form-control"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "prioridad": forms.NumberInput(attrs={"class": "form-control"}),
        }

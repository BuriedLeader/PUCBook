from django import forms
from .models import Evento

class EventoFormulario(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome','local', 'descricao','data','foto']

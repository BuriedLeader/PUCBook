from django import forms
from .models import Grupo
from .models import Usuario

class GrupoForms(forms.ModelForm):
    class Meta:
        model= Grupo
        fields = ['nome','local', 'tipo']
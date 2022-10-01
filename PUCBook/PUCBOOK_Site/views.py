from django.shortcuts import render

# Create your views here.

def ExibePerfil(request):
    return render(request, 'interface_perfil.html', {})
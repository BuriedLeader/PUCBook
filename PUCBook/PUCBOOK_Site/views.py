from django.shortcuts import render

# Create your views here.

def ExibePerfil(request):
    return render(request, 'consulta-perfil.html', {})

def ExibeLogin(request):
    return render(request, 'login.html', {})

def ExibePaginaPrincipal(request):
    return render(request, 'pagina-principal.html', {})

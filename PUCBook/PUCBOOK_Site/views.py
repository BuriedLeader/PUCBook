from django.shortcuts import render
from .models import Curso
# Create your views here.

def ExibePerfil(request):
    return render(request, 'consulta-perfil.html', {})

def ExibeLogin(request):
    return render(request, 'login.html', {})

def ExibePaginaPrincipal(request):
    return render(request, 'pagina-principal.html', {})

def ExibeCadastro(request):
    
    if request.method == "post":
        nome_usuario = request.post.get('nome_usuario')
        aniversario = request.post.get()
        curso = request.post.get()
        periodo = request.post.get()
        carona = request.post.get()
        aniversario = request.post.get()
        aniversario = request.post.get()
        aniversario = request.post.get()
        aniversario = request.post.get()
        aniversario = request.post.get()
        aniversario = request.post.get()
        aniversario = request.post.get()

    cursos_lista = Curso.objects.all()
    return render(request, 'cadastro.html', { "cursos": cursos_lista })

def ExibePaginaInicial(request):
    return render(request,'pagina-inicial.html',{})
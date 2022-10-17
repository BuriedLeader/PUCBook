from django.contrib import messages
from django.shortcuts import render
from .models import Curso, InteresseCarona, Usuario
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def ExibePerfil(request):
    return render(request, 'consulta-perfil.html', {})

def ExibeLogin(request):

    if request.method == "POST":
        login = request.POST['webmail']
        senha = request.POST['senha']

        Usuario = authenticate(webmail = login, password = senha)

        if Usuario is not None:
            login(request,Usuario)
            nome = Usuario.nome
            return render(request,'pagina-principal.html',{"nome":nome})
        else:
            messages.error(request,'Usuário e/ou Senha incorretos')
            return redirect('pagina-inicial')


    return render(request, 'login.html', {})

def ExibePaginaPrincipal(request):
    return render(request, 'pagina-principal.html', {})

def ExibeCadastro(request):
    
    if request.method == "POST":
        nome_usuario = request.POST['nome_usuario']
        aniversario = request.POST['aniversario']
        curso = request.POST['curso']
        periodo = request.POST['periodo']
        carona = request.POST['carona']
        ponto_encontro = request.POST['ponto_encontro']
        webmail = request.POST['webmail']
        senha = request.POST['senha1']
        senha_confirmada = request.POST['senha2']
        int1 = request.POST['int1']
        int2 = request.POST['int2']
        int3 = request.POST['int3']

        novo_usuario = Usuario.objects.create(nome = nome_usuario,password = senha, curso = curso, webmail=webmail)
        novo_usuario.aniversario = aniversario
        novo_usuario.periodo = periodo 
        novo_usuario.ponto_de_encontro = ponto_encontro
        novo_usuario.interesse1 = int1 
        novo_usuario.interesse2 = int2 
        novo_usuario.interesse3 = int3
        
        novo_usuario.save()

        messages.success(request,"Sua conta foi criada com sucesso")

        return redirect('login')


    cursos_lista = Curso.objects.all()
    opcoes_carona = InteresseCarona.objects.all()
    return render(request, 'cadastro.html', { "cursos": cursos_lista ,"caronas":opcoes_carona})

def ExibePaginaInicial(request):
    return render(request,'pagina-inicial.html',{})
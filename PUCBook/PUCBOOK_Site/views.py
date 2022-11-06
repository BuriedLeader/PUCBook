from tkinter.tix import Form
from django.contrib import messages
from django.shortcuts import render
from django import forms
from .models import Curso, InteresseCarona, Usuario
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout


def ExibePerfil(request):
    return render(request, 'consulta-perfil.html', {})

def ExibeLogin(request):

    if request.method == "POST":
        webmail = request.POST['webmail']
        senha = request.POST['senha']
        print(webmail)
        print(senha)

        Usuario = authenticate(username = webmail, password = senha)

        if Usuario is not None:
            login(request, Usuario)
            return redirect('/pagina-principal')
        else:
            messages.error(request,'Usuário e/ou Senha incorretos')
            return redirect('/')


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
        foto = request.POST['foto']

        '''
        if Usuario.objects.filter(nome = nome_usuario):
            messages.error(request,"Nome de usuario já existe")
            redirect(request,'pagina-inicial')

        if Usuario.objects.filter(webmail = webmail):
            messages.error(request,'webmail já está cadastrado')
            redirect(request,'pagina-inicial')

        if len(nome_usuario) > 200:
            messages.error(request,'nome muito grande')


        if senha != senha_confirmada:
            messages.error(request,'Senhas não são iguais')
        '''
        
            

        novo_usuario = Usuario.objects.create(
            webmail = webmail,
            nome = nome_usuario,
            password = senha,
        )
        novo_usuario.set_password(senha)
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

def ExibeChat(request):
    return render(request,'chat.html',{})

def ExibeEdicao(request):

    cursos_lista = Curso.objects.all()
    opcoes_carona = InteresseCarona.objects.all()

    return render(request,'edicao-perfil.html',{ "cursos": cursos_lista ,"caronas":opcoes_carona})

def ExibeRecuperarSenha1(request):

    return render(request,'recuperar-senha1.html',{})

def ExibeRecuperarSenha2(request):

    return render(request,'recuperar-senha2.html',{})
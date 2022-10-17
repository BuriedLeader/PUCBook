from email import message
from django.shortcuts import render
from .models import Curso, InteresseCarona, Usuario
from django.shortcuts import redirect,render
# Create your views here.

def ExibePerfil(request):
    return render(request, 'consulta-perfil.html', {})

def ExibeLogin(request):
    return render(request, 'login.html', {})

def ExibePaginaPrincipal(request):
    return render(request, 'pagina-principal.html', {})

def ExibeCadastro(request):
    
    if request.method == "post":
        nome_usuario = request.post['nome_usuario']
        aniversario = request.post['aniversario']
        curso = request.post['curso']
        periodo = request.post['periodo']
        carona = request.post['carona']
        ponto_encontro = request.post['ponto_encontro']
        webmail = request.post['webmail']
        senha = request.post['senha1']
        senha_confirmada = request.post['senha2']
        int1 = request.post['int1']
        int2 = request.post['int2']
        int3 = request.post['int3']

        novo_usuario = Usuario.objects.create_user(nome = nome_usuario,senha = senha, curso = curso ,aniversario = aniversario,periodo = periodo ,email = webmail,ponto_de_encontro = ponto_encontro,interesse1 = int1 ,interesse2 = int2 ,interesse3 = int3 )
        
        novo_usuario.save()

        message.success(request,"Sua conta foi criada com sucesso")

        return redirect('login')


    cursos_lista = Curso.objects.all()
    opcoes_carona = InteresseCarona.objects.all()
    return render(request, 'cadastro.html', { "cursos": cursos_lista ,"caronas":opcoes_carona})

def ExibePaginaInicial(request):
    return render(request,'pagina-inicial.html',{})
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.shortcuts import redirect, render
from .forms import EventoFormulario,RecuperarSenhaFormulario,MudarSenhaForm,EditarPerfilForm
from .models import Curso, Evento, InteresseCarona, Usuario
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required


#Verificação de email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('')

def activateEmail(request, user, to_email):
    mail_subject = 'Email de ativar conta PUCBook'
    message = render_to_string('email-confirmacao.html', {
        'user': user.nome,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, 'Email de confirmação enviado com sucesso, verifique sua conta de email. Verifique também a caixa de Spam.')
    else:
        messages.error(request, f'Problema ao enviar email para {to_email}, Verifique se o email foi digitado corretamente.')

def Deslogar(request):
    logout(request)
    messages.success(request,"usuario deslogado")
    return redirect('/')

@login_required(login_url='/login')
def ExibePerfil(request):
    return render(request, 'consulta-perfil.html', {'user':request.user})

def ExibeLogin(request):

    if request.method == "POST":
        webmail = request.POST['webmail']
        senha = request.POST['senha']

        Usuario = authenticate(username = webmail, password = senha)

        if Usuario is not None:
            login(request, Usuario)
            return redirect('/pagina-principal')
        else:
            messages.error(request,'Usuário e/ou Senha incorretos')
            return redirect('/login')


    return render(request, 'login.html', {})

@login_required(login_url='/login')
def ExibePaginaPrincipal(request):
    return render(request, 'pagina-principal.html', {'user':request.user})

def ExibeCadastro(request):
    
    if request.method == "POST":

        #Coleta de dados
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
        foto = request.FILES['foto']

        #Verificações
        if Usuario.objects.filter(nome = nome_usuario):
            messages.error(request,"Nome de usuario já existe")
            return redirect('/cadastro')

        if Usuario.objects.filter(webmail = webmail):
            messages.error(request,'webmail já está cadastrado')
            return redirect('/cadastro')
   
        if len(nome_usuario) > 200:
            messages.error(request,'nome muito grande')
            return redirect('/cadastro')

        if senha != senha_confirmada:
            messages.error(request,'Senhas não são iguais')
            return redirect('/cadastro')   

        '''
        if "@aluno.puc-rio.br" not in webmail:
            messages.error(request,'Não está utilizando um webmail de aluno da PUC')
            return redirect('/cadastro')
        '''
        
        

        if nome_usuario.isnumeric():
            messages.error(request,'Nome só possui números')
            return redirect('/cadastro')

        if webmail.isnumeric():
            messages.error(request,'email só possui números')
            return redirect('/cadastro')
        
        if len(nome_usuario) == 0:
            messages.error(request,'nome vazio')
            return redirect('/cadastro')

        if len(webmail) == 0:
            messages.error(request,'webmail vazio')
            return redirect('/cadastro')


        

        #Registro do Usuário
        novo_usuario = Usuario.objects.create(
            webmail = webmail,
            nome = nome_usuario,
            password = senha,
        )
        novo_usuario.set_password(senha)
        novo_usuario.aniversario = aniversario
        novo_usuario.bio = ''
        novo_usuario.carona = carona
        novo_usuario.curso = curso
        novo_usuario.periodo = periodo 
        novo_usuario.ponto_de_encontro = ponto_encontro
        novo_usuario.interesse1 = int1 
        novo_usuario.interesse2 = int2 
        novo_usuario.interesse3 = int3
        novo_usuario.foto = foto
        novo_usuario.is_active = False
        
        novo_usuario.save()

        activateEmail(request, novo_usuario, webmail)

        messages.success(request,"Sua conta foi criada com sucesso")


        return redirect('login')

    cursos_lista = Curso.objects.all()
    opcoes_carona = InteresseCarona.objects.all()
    return render(request, 'cadastro.html', { "cursos": cursos_lista ,"caronas":opcoes_carona})

def ExibePaginaInicial(request):
    return render(request,'pagina-inicial.html',{})

@login_required(login_url='/login')
def ExibeChat(request):
    return render(request,'chat.html',{})

@login_required(login_url='/login')
def ExibeEdicao(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST,request.FILES,instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect('/consulta-perfil')
    else:
        form = EditarPerfilForm(request.FILES,instance = request.user)

    return render(request,'edicao-perfil.html',{ 'form':form})

def ExibeRecuperarSenha(request):

    return render(request,'recuperar-senha.html',{})

@login_required(login_url='/login')
def ExibeBuscaGrupo(request):
    return render(request,'busca-grupo.html',{})

@login_required(login_url='/login')
def ExibeCadastroEvento(request):
    
    if request.method=='POST':
        formulario = EventoFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            evento = formulario.save(commit = False)
            evento.criador = request.user
            evento = formulario.save()

            return redirect('eventos')
    else:
        formulario = EventoFormulario(request.FILES)

    return render(request,'criar-evento.html',{'form':formulario,})

@login_required(login_url='/login')
def MudarSenha(request):
    user = request.user
    if request.method == 'POST':
        form = MudarSenhaForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sua senha foi alterada")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = MudarSenhaForm(user)
    return render(request, 'mudar-senha-confirmacao.html', {'form': form})

def ResetarSenha(request):
    if request.method == 'POST':
        form = RecuperarSenhaFormulario(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(webmail=user_email)).first()
            if associated_user:
                subject = "Mudança de senha"
                message = render_to_string("recuperar-senha-confirmacao.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.webmail])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Email de recuperação de senha enviado</h2><hr>
                        <p>
                            Nós enviamos um email para você com instruções para recuperar sua senha.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problema ao resetar a senha")

            return redirect('/')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "Faça a verificação de CAPTCHA")
                continue

    form = RecuperarSenhaFormulario()
    return render(
        request=request, 
        template_name="recuperar-senha.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = MudarSenhaForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Nova senha definida")
                return redirect('/')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = MudarSenhaForm(user)
        return render(request, 'mudar-senha-confirmacao.html', {'form': form,})
    else:
        messages.error(request, "Link expirou")

    messages.error(request, 'Algo deu errado, você será redirecionado para a página inicial')
    return redirect("/")

@login_required(login_url='/login')
def ExibeAmigos(request):

    return render(request,'amigos.html',{})

@login_required(login_url='/login')
def AdicionaAmigos(request):

    if request.method == 'POST':

        busca = request.POST['UsuarioBuscado']

        usuarios = Usuario.objects.filter(nome__contains = busca)

        return render(request,'adicionar-amigos.html',{'usuarios':usuarios,'busca':busca})

    else:
        usuarios = Usuario.objects.all()

        return render(request,'adicionar-amigos.html',{'usuarios':usuarios})

def ExibeEventos(request):
    if request.method == 'POST':

        busca = request.POST['EventoBuscado']
        eventos = Evento.objects.filter(nome__contains = busca)

        return render(request,'busca-eventos.html',{'busca':busca,'eventos':eventos})

    else:
        eventos = Evento.objects.all()

        return render(request,'eventos.html',{'eventos':eventos})

def BuscaEventos(request):

    if request.method == 'POST':

        busca = request.POST['EventoBuscado']
        eventos = Evento.objects.filter(nome__contains = busca)

        return render(request,'busca-eventos.html',{'busca':busca,'eventos':eventos})
    
    else:
        return render(request,'busca-eventos.html',{})

    
    
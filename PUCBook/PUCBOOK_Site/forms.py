from django import forms
from .models import Evento,Usuario
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class EventoFormulario(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome','local', 'descricao','data','foto']

class RecuperarSenhaFormulario(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class MudarSenhaForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['senha']

class EditarPerfil(forms.ModelForm):
    opcoes_curso = (
    (("1"),("Administração")),
    (("2"),("Arquitetura e Urbanismo")),
    (("3"),("Artes Cênicas")),
    (("4"),("Ciência da Computação")),
    (("5"),("Ciências Biológicas")),
    (("6"),("Ciências Econômicas (Economia)")),
    (("7"),("Ciências Sociais (Sociologia)")),
    (("8"),("Comunicação Social")),
    (("9"),("Design")),
    (("10"),("Direito")),
    (("11"),("Engenharia Ambiental")),
    (("12"),("Engenharia Civil")),
    (("13"),("Engenharia da Computação")),
    (("14"),("Engenharia de Controle e Automação")),
    (("15"),("Engenharia Elétrica")),
    (("16"),("Engenharia de Materiais e Nanotecnologia")),
    (("17"),("Engenharia Mecânica")),
    (("18"),("Engenharia de Petróleo")),
    (("19"),("Engenharia de Produção")),
    (("20"),("Engenharia Química")),
    (("21"),("Estudos de Mídia")),
    (("22"),("Filosofia")),
    (("23"),("Física")),
    (("24"),("Geografia")),
    (("25"),("História")),
    (("26"),("Jornalismo")),
    (("27"),("Letras")),
    (("28"),("Matemática")),
    (("29"),("Neurociências ")),
    (("30"),("Nutrição ")),
    (("31"),("Pedagogia")),
    (("32"),("Psicologia")),
    (("33"),("Química")),
    (("34"),("Relações Internacionais")),
    (("35"),("Serviço Social")),
    (("36"),("Sistemas de Informação")),
    (("37"),("Tecnológico em Gestão Financeira ")),
    (("38"),("Teologia"))
    ,)
    pontos = ((('1'),('Busco Carona')),(('2'),('Ofereço Carona')),(('3'),('Busco e Ofereço Carona')),)
    curso = forms.ChoiceField(choices=opcoes_curso)
    class Meta:
        model = Usuario
        fields = ['nome','curso','periodo','ponto_de_encontro', 'carona']

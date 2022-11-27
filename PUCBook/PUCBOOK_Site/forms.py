from django import forms
from .models import Evento,Usuario
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm,UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class DateInput(forms.DateInput):
    input_type = 'date'

class EventoFormulario(forms.ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
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



class EditarPerfilForm(forms.ModelForm):
    opcoes_curso = (
    (("Administração"),("Administração")),
    (("Arquitetura e Urbanismo"),("Arquitetura e Urbanismo")),
    (("Artes Cênicas"),("Artes Cênicas")),
    (("Ciência da Computação"),("Ciência da Computação")),
    (("Ciências Biológicas"),("Ciências Biológicas")),
    (("Ciências Econômicas (Economia)"),("Ciências Econômicas (Economia)")),
    (("Ciências Sociais (Sociologia)"),("Ciências Sociais (Sociologia)")),
    (("Comunicação Social"),("Comunicação Social")),
    (("Design"),("Design")),
    (("Direito"),("Direito")),
    (("Engenharia Ambiental"),("Engenharia Ambiental")),
    (("Engenharia Civil"),("Engenharia Civil")),
    (("Engenharia da Computação"),("Engenharia da Computação")),
    (("Engenharia de Controle e Automação"),("Engenharia de Controle e Automação")),
    (("Engenharia Elétrica"),("Engenharia Elétrica")),
    (("Engenharia de Materiais e Nanotecnologia"),("Engenharia de Materiais e Nanotecnologia")),
    (("Engenharia Mecânica"),("Engenharia Mecânica")),
    (("Engenharia de Petróleo"),("Engenharia de Petróleo")),
    (("Engenharia de Produção"),("Engenharia de Produção")),
    (("Engenharia Química"),("Engenharia Química")),
    (("Estudos de Mídia"),("Estudos de Mídia")),
    (("Filosofia"),("Filosofia")),
    (("Física"),("Física")),
    (("Geografia"),("Geografia")),
    (("História"),("História")),
    (("Jornalismo"),("Jornalismo")),
    (("Letras"),("Letras")),
    (("Matemática"),("Matemática")),
    (("Neurociências"),("Neurociências")),
    (("Nutrição"),("Nutrição")),
    (("Pedagogia"),("Pedagogia")),
    (("Psicologia"),("Psicologia")),
    (("Química"),("Química")),
    (("Relações Internacionais"),("Relações Internacionais")),
    (("Serviço Social"),("Serviço Social")),
    (("Sistemas de Informação"),("Sistemas de Informação")),
    (("Tecnológico em Gestão Financeira"),("Tecnológico em Gestão Financeira")),
    (("Teologia"),("Teologia"))
    ,)
    caronas = ((('Busco Carona'),('Busco Carona')),(('Ofereço Carona'),('Ofereço Carona')),(('Busco e Ofereço Carona'),('Busco e Ofereço Carona')),)
    curso = forms.ChoiceField(choices=opcoes_curso)
    carona = forms.ChoiceField(choices = caronas)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Usuario
        fields = ['bio','carona','curso','periodo','ponto_de_encontro','foto']


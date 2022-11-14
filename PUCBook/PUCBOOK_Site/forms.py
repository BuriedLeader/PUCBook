from django import forms
from .models import Evento
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

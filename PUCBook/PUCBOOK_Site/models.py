from django.conf import settings
from django.db import models
from django.utils import timezone

class Mensagem(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data_envio = models.DateTimeField(blank=True, null=True)

    def enviar(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.texto

class CaixaComInformacoes(models.Model):
    titulo = "Titulo" + "\n"
    texto = models.TextField()

    def __str__(self):
        return titulo + self.texto

class Carona(models.Model):
    meio_de_transporte = ""
    valor = 0
    rota = ""

class Grupo(models.Model):
    tipo = ""
    quantidade_membros = 0
    adm = ""


class Usuario(models.Model):

    idade = models.IntegerField(default=0)
    curso = models.CharField(max_length = 200)
    aniversario = ""
    periodo = 1
    email = "@aluno.puc-rio.br"
    ponto_de_encontro = ""

    

    
from django.conf import settings
from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nome = models.CharField(max_length = 200)
    senha = models.CharField(max_length = 200)
    idade = models.IntegerField(default=0)
    curso = models.CharField(max_length = 200)
    aniversario = models.CharField(max_length = 10)
    periodo = models.IntegerField(default=0)
    email = models.CharField(max_length = 200)
    ponto_de_encontro = models.CharField(max_length = 200)
    interesse1 = models.CharField(max_length = 200)
    interesse2 = models.CharField(max_length = 200)
    interesse3 = models.CharField(max_length = 200)

class Curso(models.Model):
    nome = models.CharField(max_length = 100)
    def __str__(self):
        return self.nome



    
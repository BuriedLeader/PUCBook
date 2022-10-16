from email.policy import default
from operator import mod
from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length = 100)
    idade = models.IntegerField()
    aniversario = models.DateField()
    periodo = models.IntegerField()
    email = models.CharField(max_length = 200)
    ponto_de_encontro = models.CharField(max_length = 200)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 100)
    def __str__(self):
        return self.nome



    
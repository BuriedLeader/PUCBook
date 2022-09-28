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
    
from distutils.command.upload import upload
from multiprocessing.reduction import send_handle
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager



class CustomAccountManager(BaseUserManager):

    def create_superuser(self,webmail,nome,password, **other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser tem que ser staff')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser tem que ser um superuser')

        return self.create_user(webmail,nome,password, **other_fields)
    
    def create_user(self,webmail,nome, password, **other_fields):

        if not webmail:
            raise ValueError(_('Me dê um endereço de email'))

        webmail = self.normalize_email(webmail)
        user = self.model(webmail = webmail,nome = nome, **other_fields)
        user.set_password(password)
        user.save(using = self._db)


        return user

        
    

class Usuario(AbstractBaseUser,PermissionsMixin):
    aniversario = models.DateField(_('aniversario'),default = timezone.now,editable= False)
    bio = models.CharField(_('bio'),max_length=200,default = '')
    carona = models.CharField(_('carona'),max_length=80)
    curso = models.CharField(_('curso'),max_length = 200)
    foto = models.ImageField(upload_to = 'images',default = 'images/perfil_vazio.jpeg')
    interesse1 = models.CharField(_('interesse1'),max_length = 200)
    interesse2 = models.CharField(_('interesse2'),max_length = 200)
    interesse3 = models.CharField(_('interesse3'),max_length = 200)
    nome = models.CharField(_('nome'),max_length = 200, unique = True, blank = True,editable= False)
    ponto_de_encontro = models.CharField(_('ponto_encontro'),max_length = 200)
    periodo = models.IntegerField(_('periodo'),default=0)
    webmail = models.EmailField(_('webmail'),max_length = 200,unique = True,editable= False)

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = 'webmail'
    REQUIRED_FIELDS = ['nome']

    objects = CustomAccountManager()

    def __str__(self):
        return self.nome


class InteresseCarona(models.Model):
    tipo = models.CharField(max_length = 100)
    def __str__(self):
        return self.tipo

class Curso(models.Model):
    nome = models.CharField(max_length = 100)
    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    data = models.DateField(default = timezone.now)
    foto = models.ImageField(upload_to = 'images',default = 'images/imagem_em_branco.jpg')

    def __str__(self):
        return self.nome


    


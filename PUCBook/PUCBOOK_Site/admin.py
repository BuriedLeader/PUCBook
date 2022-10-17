from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Curso)
admin.site.register(Usuario)
admin.site.register(InteresseCarona)
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

'''
class UserAdminConfig(UserAdmin):
    search_fields = ('nome','webmail','curso')
    ordering = ("-nome",)
    list_display = ('nome','webmail','curso','aniversario','periodo','is_staff')
'''


admin.site.register(Curso)
admin.site.register(Usuario)
admin.site.register(InteresseCarona)
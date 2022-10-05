from django.urls import path
from . import views

urlpatterns = [
    path('login', views.ExibeLogin, name='login'),
    path('pagina-principal', views.ExibePaginaPrincipal, name='pagina-principal'),
    path('consulta-perfil', views.ExibePerfil, name='consulta-perfil'),
    path('cadastro', views.ExibePerfil, name='cadastro-usuario')
]
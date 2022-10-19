from django.urls import path
from . import views

urlpatterns = [
    path('pagina-inicial', views.ExibePaginaInicial, name='Bem-vindo ao PUCBook'),
    path('login', views.ExibeLogin, name='login'),
    path('pagina-principal', views.ExibePaginaPrincipal, name='pagina-principal'),
    path('consulta-perfil', views.ExibePerfil, name='consulta-perfil'),
    path('cadastro', views.ExibeCadastro, name='cadastro-usuario'),
    path('chat', views.ExibeChat, name='chat')
]
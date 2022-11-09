from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExibePaginaInicial, name='Bem-vindo ao PUCBook'),
    path('Deslogar',views.Deslogar),
    path('login', views.ExibeLogin, name='login'),
    path('pagina-principal', views.ExibePaginaPrincipal, name='pagina-principal'),
    path('consulta-perfil', views.ExibePerfil, name='consulta-perfil'),
    path('cadastro', views.ExibeCadastro, name='cadastro-usuario'),
    path('chat', views.ExibeChat, name='chat'),
    path('edicao-perfil', views.ExibeEdicao, name='edicao-perfil'),
    path('recuperar-senha', views.ExibeRecuperarSenha1, name='recuperar-senha'),
    path('recuperar-senha2', views.ExibeRecuperarSenha2, name='recuperar-senha2'),
    path('grupos', views.grupo, name='grupo'),
    path('busca-grupo',views.ExibeBuscaGrupo,name = 'busca-grupo')
]
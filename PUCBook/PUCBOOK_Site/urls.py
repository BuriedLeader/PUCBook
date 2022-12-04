from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ExibePaginaInicial, name='Bem-vindo ao PUCBook'),
    path('Deslogar',views.Deslogar),
    path('login', views.ExibeLogin, name='login'),
    path('pagina-principal', views.ExibePaginaPrincipal, name='pagina-principal'),
    path('consulta-perfil', views.ExibePerfil, name='consulta-perfil'),
    path('cadastro', views.ExibeCadastro, name='cadastro'),
    path('chat', views.ExibeChat, name='chat'),
    path('edicao-perfil', views.ExibeEdicao, name='edicao-perfil'),
    path('eventos',views.ExibeEventos,name = 'eventos'),
    path('busca-evento',views.BuscaEventos,name = 'busca-evento'),
    path("mudar-senha", views.MudarSenha, name="mudar-senha"),
    path('recuperar-senha', views.ResetarSenha, name='recuperar-senha'),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('criar-evento', views.ExibeCadastroEvento, name='criar-evento'),
    path('busca-grupo',views.ExibeBuscaGrupo,name = 'busca-grupo'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('amigos',views.ExibeAmigos,name = 'amigos'),
    path('adicionar-amigos',views.AdicionaAmigos,name = 'adicionar amigos')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
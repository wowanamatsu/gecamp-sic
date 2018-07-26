from django.urls import path

from .views import home, login, paises

urlpatterns = [
    path('', home.index, name='home'),
    path('sobre/', home.sobre, name='sobre'),
]

# Rotas para a pagina de Login
urlpatterns +=[
    path('login/', login.logar, name='login'),
    path('logout/', login.deslogar, name='logout'),
]

# Rotas para paises
urlpatterns += [
    path('paises/', paises.paises, name='paises'),
    path('pais/novo/', paises.novo, name='cadastrar_pais'),
    path('pais/<int:id>', paises.exibir, name='exibir_pais'),
    path('pais/<int:id>/edit', paises.atualizar, name='atualizar_pais'),
    path('pais/<int:id>/delete', paises.deletar, name='deletar_pais'),

    path('api/', paises.api, name='teste'),
    path('pdf/', paises.pdf, name='pdf'),
    path('teste/', paises.teste, name='teste'),
]
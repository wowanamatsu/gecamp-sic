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
    path('paises/', paises.paises, name='paises')
]
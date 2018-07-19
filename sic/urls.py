from django.urls import path

from .views import home

urlpatterns = [
    path('', home.index, name='home'),
    path('sobre/', home.sobre, name='sobre'),
]


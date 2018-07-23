from django.shortcuts import render
from ..models import Pais

def paises(request):
    paises = Pais.objects.all()
    return render(request, 'paises/index.html', {'paises':paises})
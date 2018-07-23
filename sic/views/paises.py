from django.shortcuts import render
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse

from ..models import Pais

def paises(request):
    paises = Pais.objects.all()

    paginator = Paginator(paises, 10)

    page = request.GET.get('page')

    paises = paginator.get_page(page)

    return render(request, 'paises/index.html', {'paises':paises})


def teste(request):
    paises = Pais.objects.all()
    return render(request, 'paises/datatables.html', {'paises':paises})

def api(request):
    paises = Pais.objects.all()
    json = serializers.serialize('json', paises)

    return HttpResponse(json, content_type='application/json')
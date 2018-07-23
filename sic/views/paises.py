from django.shortcuts import render
from django.core.paginator import Paginator

from ..models import Pais

def paises(request):
    paises = Pais.objects.all()

    paginator = Paginator(paises, 10)

    page = request.GET.get('page')

    paises = paginator.get_page(page)

    return render(request, 'paises/index.html', {'paises':paises})
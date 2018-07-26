from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse

from ..models import Pais

from ..forms import PaisForm

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

def pdf(request):
    from io import BytesIO
    from reportlab.pdfgen import canvas
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdfs.pdf"'

    buffer = BytesIO()

    paises = Pais.objects.all()

    p = canvas.Canvas(buffer)

    y = 0
    for pais in paises:
        y += 20
        p.drawString(100, (100 + y), pais.nome)

    p.showPage()
    p.save()

    pdf = buffer.getbuffer()
    buffer.close()
    response.write(pdf)

    return response



def novo(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paises')
    else:
        form = PaisForm()
    return render(request, 'paises/_form.html', {'form':form})


def exibir(request, id):
    pais = get_object_or_404(Pais, id=id)
    return render(request, 'paises/exibir.html', {'pais':pais})


def atualizar(request, id):
    updatePais = get_object_or_404(Pais, id=id)
    form = PaisForm(request.POST, instance=updatePais)

    if form.is_valid():
        form.save()
        return redirect('paises')

    form = PaisForm(instance=updatePais)

    return render(request, 'paises/_form.html', {'form':form})


def deletar(request, id):
    instance = Pais.objects.get(id=id).delete()
    return redirect('paises')





















from django.shortcuts import render, redirect, get_object_or_404

from ..models import Estado
from ..forms import EstadoForm

def index(request):
    estados = Estado.objects.all()
    return render(request, 'estados/index.html', {'estados':estados})


def novo(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estados')
    else:
        form = EstadoForm
    return render(request, 'estados/_form.html', {'form':form})


def exibir(request, id):
    estado = Estado.objects.get(pk=id)
    return render(request, 'estados/exibir.html', {'estado':estado})


def atualizar(request, id):
    estado = get_object_or_404(Estado, id=id)
    form = EstadoForm(request.POST, instance=estado)

    if form.is_valid():
        form.save()
        return redirect('estados')

    form = EstadoForm(instance=estado)

    return  render(request, 'estados/_form.html', {'form':form})


def deletar(request, id):
    estado = Estado.objects.get(id=id).delete()
    return redirect('estados')
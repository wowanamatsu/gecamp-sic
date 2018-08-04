from django.shortcuts import render, redirect

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
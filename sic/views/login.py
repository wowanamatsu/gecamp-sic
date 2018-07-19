from django.shortcuts import render

def logar(request):
    return render(request, 'login.html')
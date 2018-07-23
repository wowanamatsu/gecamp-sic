from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse

def logar(request):
    if request.method == 'POST': print('CSRF: {}\nUsuário: {}'.format(request.POST['csrfmiddlewaretoken'],request.POST['username']))
    if request.user.is_authenticated:
       return redirect('home')

    if request.method == 'POST':
        error = []
        usuario = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=usuario, password=senha)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            error.append('Usuário ou senha incorretos.')
            return JsonResponse({'data':error})
            # return render(request, 'login.html', {'erros':error})
    return render(request, 'login.html')



def deslogar(request):
    logout(request)
    return redirect('login.html')
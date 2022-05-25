from django.shortcuts import render


def inicio(request):
    return render(request, 'appcoins/inicio.html', context={
        'name': 'Testando',
    })

def sobre(request):
    return render(request,'appcoins/sobre.html')

def servicos(request):
    return render(request, 'appcoins/servicos.html')

def contato(request):
    return render(request, 'appcoins/contato.html')
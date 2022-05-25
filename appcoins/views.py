from django.shortcuts import render
from django.http import HttpResponse



def inicio(request):
    return render(request, 'appcoins/inicio.html')

def sobre(request):
    return HttpResponse('Sobre o site')

def servicos(request):
    return HttpResponse('Serviços do site')

def contato(request):
    return HttpResponse('Contato do site')
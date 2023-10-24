from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Buscaminas/index.html')

def tablero(request):
    return render(request, 'Buscaminas/crea_tablero.html')

from django.shortcuts import render
from .forms import CreaTableroForm
# Create your views here.

def index(request):
    return render(request, 'Buscaminas/index.html')


def crea_tablero(request):
    if request.method == 'POST':
        tablero_form = CreaTableroForm(request.POST)

        if(tablero_form.is_valid()):
            columnas = tablero_form.cleaned_data['columnas']
            filas = tablero_form.cleaned_data['filas']
            nMinas = tablero_form.cleaned_data['nMinas']
            return render(request, 'Buscaminas/muestra_tablero.html', 
                                  {'filas':filas, 'columnas':columnas, "nMinas":nMinas, 
                                  'rango_filas':range(filas), 'rango_columnas':range(columnas)})
    else:
      tablero_form = CreaTableroForm()
    return render(request, 'Buscaminas/crea_tablero.html', {'form':tablero_form })

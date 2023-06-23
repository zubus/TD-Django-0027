from django.shortcuts import render
from django.http import HttpResponse
#importar vista basada en clase
from django.views.generic import TemplateView
#numero entero aleatorio
from random import randint
#libreria para el manejo de las fechas
import datetime




# Clase Para ejemplificar
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Hola Mundo, desde la app boards</h1>")

class IndexView(TemplateView):
    template_name = "boards/index.html"  #buscamos dentro de la carpeta templates(de boards),
    # la carpeta boards y dentro un archivo llamado index.html

def get_date_view(request, name):
    fecha_actual = datetime.datetime.now()
    context = {
        'fecha': fecha_actual,
        'nombre':name,
        'frutas': ["Platano", "Durazno", "Manzana", "Naranja"],
        'aleatorio':randint(0,9),
        }
    return render(request,'boards/fecha.html', context)
        #  render(request, template, datos(context[diccionario]))

def name_view(request):
    return render(request, 'boards/nombre.html')

def mostrar(request):
    persona = Persona("Juan", "Perez")
    context = {"persona": persona}
    return render(request, "boards/example.html",context)
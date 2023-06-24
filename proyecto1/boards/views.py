from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#importar vista basada en clase
from django.views.generic import TemplateView
#numero entero aleatorio
from random import randint
#Formulario
from .forms import NameForm,AuthorForm, InputForm
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
    if request.method == 'POST':
        context = {"nombre" :request.POST["your_name"]}
        return render(request, 'boards/nombre.html', context)
    return render(request, 'boards/nombre.html')

def mostrar(request):
    persona = Persona("Juan", "Perez")
    context = {"persona": persona}
    return render(request, "boards/example.html",context)

def formulario_nombre(request):
    return render(request, 'boards/formulario1.html')

def get_name(request):
    #logica de si se trata de una solicitud post
    if request.method == 'POST':
        #crear una instancia del formulario con los datos ingresados
        form = NameForm(request.POST)
        if form.is_valid():
            #aqui se hace lo que queramos con los datos
            #procesamos los datos
            return HttpResponseRedirect('/thanks/')
    else:
        #si es un metodo get
        form = NameForm()
        context= {'form':form}
        return render(request, 'boards/name.html',context)


def thanks(request):
    return render(request, "boards/gracias.html")


def create_author(request):
    #logica de si se trata de una solicitud post
    if request.method == 'POST':
        #crear una instancia del formulario con los datos ingresados
        form = AuthorForm(request.POST)
        if form.is_valid():
            #aqui se hace lo que queramos con los datos
            #procesamos los datos
            form.save() #guardando los datos ingresados en la bd
            return HttpResponseRedirect('/thanks/')
    else:
        #si es un metodo get
        form = AuthorForm()
        context= {'form':form}
        return render(request, 'boards/author.html',context)

def datosform_view(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'boards/datosform.html', context)
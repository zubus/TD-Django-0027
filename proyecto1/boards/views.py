from django.shortcuts import render
from django.http import HttpResponse
#importar vista basada en clase
from django.views.generic import TemplateView
#libreria para el manejo de las fechas
import datetime


# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Hola Mundo, desde la app boards</h1>")

class IndexView(TemplateView):
    template_name = "boards/index.html"  #buscamos dentro de la carpeta templates(de boards),
    # la carpeta boards y dentro un archivo llamado index.html

def get_date_view(request):
    fecha_actual = datetime.datetime.now()
    context = {'fecha': fecha_actual}
    return render(request,'boards/fecha.html', context)
        #  render(request, template, datos(context[diccionario]))
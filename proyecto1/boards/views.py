from django.shortcuts import render
from django.http import HttpResponse
#importar vista basada en clase
from django.views.generic import TemplateView
# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Hola Mundo, desde la app boards</h1>")

class IndexView(TemplateView):
    template_name = "boards/index.html"
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#importar vista basada en clase
from django.views.generic import TemplateView
#numero entero aleatorio
from random import randint
#Formulario
from .forms import NameForm,AuthorForm, InputForm, UserRegisterForm
#importamos para la vista de registro de ususarios
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
#se agrega authenticate y el formulario para el login en nuestro sistema
from django.contrib.auth.forms import AuthenticationForm
#para la gestion de permisos
from .models import Boards
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
#required mixins
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
#para las vistas basadas en funciones podemos usar otras herramientas
from django.contrib.auth.decorators import login_required, permission_required
#libreria para el manejo de las fechas
import datetime




# Clase Para ejemplificar
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Create your views here.
@login_required(login_url='/login/')
def index_view(request):
    return HttpResponse("<h1>Hola Mundo, desde la app boards</h1>")

class IndexView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    login_url = '/login/'
    permission_required = 'boards.es_miembro_1'
    template_name = "boards/index.html"  #buscamos dentro de la carpeta templates(de boards),
    # la carpeta boards y dentro un archivo llamado index.html

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def formulario_nombre(request):
    return render(request, 'boards/formulario1.html')

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
@permission_required(perm='boards.es_miembro_1', raise_exception=True)
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

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #obtenemos el contenttype del modelo
            content_type = ContentType.objects.get_for_model(Boards)
            #obtenemos el permiso a asignar
            es_miembro_1 = Permission.objects.get(
                codename='es_miembro_1',
                content_type=content_type
            )
            user = form.save() #aqui ya tenemos el objeto User
            user.user_permissions.add(es_miembro_1)

            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente")
        else:
            messages.error(request, "Registro Invalido. Algunos datos ingresados no son correctos")
        return HttpResponseRedirect('/thanks')

    form = UserRegisterForm()
    context = {"register_form":form}
    return render(request, 'boards/register.html',context)


def login_view(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #si existe el usuario devuelve el objeto
            #si no existe el usuario, o no autentifica devuelve None
            if user is not None:
                login(request, user)
                messages.info(request, f"iniciaste sesion como {username}.")
                return HttpResponseRedirect("/thanks/")
            else:
                messages.error(request, "username o password incorrectos")
                return HttpResponseRedirect("/login/")
        else:
            messages.error(request, "username o password incorrectos")
            return HttpResponseRedirect("/login/")

    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request, 'boards/login.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, " se ha cerrado la sesion satisfactoriamente")
    return HttpResponseRedirect('/login/')
from django.urls import path
from .views import (
    index_view,
    IndexView, 
    get_date_view, 
    name_view,
    mostrar,
    formulario_nombre,
    get_name,
    thanks,
    )
# from . import views

urlpatterns = [
    path("", index_view, name="index"),
    path("template/", IndexView.as_view(), name="index_class"),
    path("date/<str:name>/", get_date_view, name="get_date"),
    path("name/", name_view, name="name"),
    path("example/", mostrar, name="example"),
    path("formulario/", formulario_nombre, name="formulario"),
    path("getname/", get_name, name="get_name"),
    path("thanks/", thanks, name="thanks"),

]

#tag permiten realizar funciones de Django  {url ->name}
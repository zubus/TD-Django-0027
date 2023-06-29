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
    create_author,
    datosform_view,
    register_view,
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
    path("createauthor/", create_author, name="create_author"),
    path("datosform/", datosform_view, name="datosform"),
    path("register/", register_view, name="register"),
]

#tag permiten realizar funciones de Django  {url ->name}
from django.urls import path

from .views import (IndexView, create_author, datosform_view,
                    formulario_nombre, get_date_view, get_name, index_view,
                    login_view, logout_view, mostrar, name_view, register_view,
                    thanks)

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
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

#tag permiten realizar funciones de Django  {url ->name}
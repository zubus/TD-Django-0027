from django.urls import path
from .views import index_view, IndexView, get_date_view
# from . import views

urlpatterns = [
    path("", index_view, name="index"),
    path("template/", IndexView.as_view(), name="index_class"),
    path("date/<str:name>/", get_date_view, name="get_date"),
]

#tag permiten realizar funciones de Django  {url ->name}
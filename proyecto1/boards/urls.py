from django.urls import path
from .views import index_view, IndexView
# from . import views

urlpatterns = [
    path("", index_view, name="index"),
    path("template/", IndexView.as_view(), name="index"),
]

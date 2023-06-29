from django import forms
from django.forms import ModelForm
from .models import Author, Book
#agregamos para el registro de usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NameForm(forms.Form):
    your_name = forms.CharField(label='enter your name:', max_length=100)
    
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title','birth_date']


class InputForm(forms.Form):
    nombres =  forms.CharField(max_length=200 )
    apellidos = forms.CharField(max_length=200)
    prioridad = forms.IntegerField(min_value=1, max_value=3)
    contrasena = forms.CharField(widget=forms.PasswordInput())

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email","password1", "password2")


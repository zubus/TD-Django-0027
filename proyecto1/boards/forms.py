from django import forms
from django.forms import ModelForm
from .models import Author, Book
class NameForm(forms.Form):
    your_name = forms.CharField(label='enter your name:', max_length=100)
    
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title','birth_date']
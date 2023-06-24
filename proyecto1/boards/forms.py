from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='enter your name:', max_length=100)
    pet = forms.CharField(label='enter pet name:', max_length=100)
    country = forms.CharField(label='enter your country:', max_length=100)

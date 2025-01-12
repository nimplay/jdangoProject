from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_lenght=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    Last_name =  forms.CharField(label="", max_lenght=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))



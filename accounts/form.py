from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserAccount
from django import forms

class LoginCustomUserForm(AuthenticationForm):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
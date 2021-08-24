from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserAccount
from django import forms

class CreateCustomUserForm(forms.ModelForm):
    first_name = forms.CharField(label='first name', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    last_name = forms.CharField(label='first name', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = UserAccount
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password and confirm password does not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginCustomUserForm(AuthenticationForm):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
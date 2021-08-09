from django.forms import ModelForm
from .models import product
from django import forms

class productForm(ModelForm):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    description = forms.CharField(label='description', widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'text'}))
    class Meta:
        model = product
        fields = '__all__'
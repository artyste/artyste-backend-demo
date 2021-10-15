from django.forms import ModelForm
from .models import product
from django import forms

class productForm(ModelForm):
    FIAT_STATUS = [
        (2, 'SOL'),
        (1, 'U.S. Dollar'),
    ]
    title = forms.CharField(label='title', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    description = forms.CharField(label='description', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'style': "height: 100px"}))
    fileimage = forms.FileField(label='Image or Video', required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'type': "file", 'id': 'file' }))
    fiat = forms.ChoiceField(label='Fiat', required=True, widget=forms.Select(attrs={'class': 'form-select', 'type': 'select', }), choices=FIAT_STATUS)
    price = forms.FloatField(label='Price', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    royalty = forms.FloatField(label='Price', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))

    class Meta:
        model = product
        fields = ['title', 'description', 'fileimage', 'price', 'fiat', 'royalty']

class productFormArtistUpdate(ModelForm):
    FIAT_STATUS = [
        (0, 'Ethereum'),
        (1, 'U.S. Dollar'),
    ]
    title = forms.CharField(label='title', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    description = forms.CharField(label='description', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'style': "height: 100px"}))
    fileimage = forms.FileField(label='Image or Video', required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'type': "file", 'id': 'file' }))
    fiat = forms.ChoiceField(label='Fiat', required=True, widget=forms.Select(attrs={'class': 'form-select', 'type': 'select', }), choices=FIAT_STATUS)
    price = forms.FloatField(label='Price', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    royalty = forms.FloatField(label='Price', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))

    class Meta:
        model = product
        fields = ['title', 'description', 'fileimage', 'price', 'fiat', 'royalty']
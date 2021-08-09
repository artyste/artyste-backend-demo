from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import product
from .forms import productForm

# Create your views here.
# @login_required(login_url='login')
def pagehome(request):
    context = {}

    return render(request, 'art/home.html', context)

def pageartworks(request):
    context = {}
    user = request.user
    artworks_get = product.objects.filter(artist=user)
    context['artworks'] = artworks_get
    return render(request, 'art/artworks.html', context)

def pageartworksnew(request):
    form = productForm()
    context = {}
    context['form'] = form
    return render(request, 'art/artworks-new.html', context)
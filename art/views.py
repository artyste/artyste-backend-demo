from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import product, gallery
from .forms import productForm
from django.views.generic.detail import DetailView
import json

# Create your views here.
# @login_required(login_url='login')
def pagehome(request):
    context = {}
    galleries_get = gallery.objects.all()
    products_get = product.objects.all()
    context['galleries'] = galleries_get
    context['products'] = products_get
    return render(request, 'art/home.html', context)

def pagegalleries(request):
    context = {}
    galleries_get = gallery.objects.all()
    context['galleries'] = galleries_get
    return render(request, 'art/galleries.html', context)

def pageartworks(request):
    context = {}
    user = request.user
    artworks_get = product.objects.filter(artist=user)
    context['artworks'] = artworks_get
    return render(request, 'art/artworks.html', context)

def pageartworksnew(request):
    form = productForm()
    context = {}

    user = request.user

    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            new_artwork = form.save(commit=False)
            new_artwork.artist = user
            new_artwork.save()
            return redirect('artworks')


    context['form'] = form
    return render(request, 'art/artworks-new.html', context)



class pageproductdetail(DetailView):
    model = product
    template_name = 'art/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class pagegallerydetail(DetailView):
    model = gallery
    template_name = 'art/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def pageproductmint(request, pk):
    context = {}
    print(pk)
    artworks_get = product.objects.get(pk=pk)

    if request.method == 'POST':
        data = json.loads(request.body)
        artworks_get.mintingstatus = 1
        artworks_get.mintingtx = data['tx']
        artworks_get.save()


    context['product'] = artworks_get
    return render(request, 'art/mint.html', context)


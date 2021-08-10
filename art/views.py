from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import product, gallery
from .forms import productForm
from django.views.generic.detail import DetailView

# Create your views here.
# @login_required(login_url='login')
def pagehome(request):
    context = {}
    galleries_get = gallery.objects.all()
    context['galleries'] = galleries_get
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



class pagegallerydetail(DetailView):
    model = gallery
    template_name = 'art/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class pagegalleryvrdetail(DetailView):
    model = gallery
    template_name = 'art/gallery-vr.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
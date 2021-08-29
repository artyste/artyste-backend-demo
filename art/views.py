from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import product, gallery
from .forms import productForm
from django.views.generic.detail import DetailView
import json
import uuid
import requests
import os

# Create your views here.
# @login_required(login_url='login')
def pagehome(request):
    context = {}
    galleries_get = gallery.objects.all()
    products_get = product.objects.all()
    context['galleries'] = galleries_get
    context['products'] = products_get



    try:
        CIRCLEAPIKEY = os.getenv('ARTHOLOGY_CIRCLE_SANDBOX')

        url = 'https://api-sandbox.circle.com/v1/wallets/' + request.user.circle_walletId

        headers = {
            'Accept': 'application/json',
            'Authorization': "Bearer " + CIRCLEAPIKEY,
        }

        response = requests.get(url, headers=headers)
        responseJson = response.json()
        print(responseJson)
        print(responseJson['data']['balances'][0]['amount'])

        context['circle'] = responseJson['data']['balances'][0]['amount']

    except:
        context['circle'] = '0.00'



    return render(request, 'art/home.html', context)

def pagegalleries(request):
    context = {}
    galleries_get = gallery.objects.all()
    context['galleries'] = galleries_get
    return render(request, 'art/galleries.html', context)

def pageartworks(request):
    context = {}
    user = request.user
    artworks_get = product.objects.filter(owner=user)
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


def pageproductdetail(request, pk):
    context = {}
    artworks_get = product.objects.get(pk=pk)

    if request.method == 'POST':
        data = json.loads(request.body)
        artworks_get.mintingstatus = 2
        artworks_get.mintinghash = data['hash']
        artworks_get.mintingid = data['id']
        artworks_get.save()

    context['product'] = artworks_get
    context['page'] = 'productdetail'
    return render(request, 'art/product.html', context)

def pagecheckout(request, pk):
    context = {}
    artworks_get = product.objects.get(pk=pk)

    if request.method == 'POST':

        CIRCLEAPIKEY = os.getenv('ARTHOLOGY_CIRCLE_SANDBOX')
        UUIDGEN = uuid.uuid4()
        url = "https://api-sandbox.circle.com/v1/cards"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + CIRCLEAPIKEY
        }

        creditCardTotal = request.POST.get('creditCardTotal')
        creditCardEncrypted = request.POST.get('creditCardEncrypted')
        creditCardName = request.POST.get('creditCardName')
        creditCardDate = request.POST.get('creditCardDate')
        billingLine1 = request.POST.get('billingLine1')
        billingLine2 = request.POST.get('billingLine2')
        billingCountry = request.POST.get('billingCountry')
        billingdistrict = request.POST.get('billingdistrict')
        billingCity = request.POST.get('billingCity')
        billingZip = request.POST.get('billingZip')

        creditCardDateYYYY = int('20' + creditCardDate[-2:])
        creditCardDateMM = int(creditCardDate[:2])
        print(creditCardDateMM)
        print(creditCardDateYYYY)

        payload = {
            "idempotencyKey": str(UUIDGEN),
            "expMonth": creditCardDateMM,
            "expYear": creditCardDateYYYY,
            "keyId": "key1",
            "encryptedData": creditCardEncrypted,
            "billingDetails": {
                "name": creditCardName,
                "country": billingCountry,
                "district": billingdistrict,
                "line1": billingLine1,
                "line2": billingLine2,
                "city": billingCity,
                "postalCode": billingZip
            },
            "metadata": {
                "email": "customer-0001@circle.com",
                "phoneNumber": "+12025550180",
                "sessionId": "xxx",
                "ipAddress": "172.33.222.1"
            }
        }
        response = requests.post(url, json=payload, headers=headers )
        responseJson = response.json()
        print(responseJson)

    context['product'] = artworks_get
    context['page'] = 'checkout'
    return render(request, 'art/checkout.html', context)

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
    context['page'] = 'productmint'
    return render(request, 'art/mint.html', context)
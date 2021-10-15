from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import product, gallery, transaction
from accounts.models import card, UserAccount
from .forms import productForm
from django.views.generic.detail import DetailView
import json
import uuid
import requests
import os

from .api.metaplex_api import MetaplexAPI
from cryptography.fernet import Fernet
import base58
from solana.account import Account
from solana.rpc.api import Client
from django.conf import settings
from django.http import JsonResponse


# Create your views here.
# @login_required(login_url='login')
def pagehome(request):
    context = {}
    galleries_get = gallery.objects.all()
    products_get = product.objects.all()
    context['galleries'] = galleries_get
    context['products'] = products_get



    try:
        CIRCLEAPIKEY = os.getenv('ARTYSTEDEMO_CIRCLE_SANDBOX')
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
            new_artwork.owner = user
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
        print('post')
        CIRCLEAPIKEY = os.getenv('ARTYSTEDEMO_CIRCLE_SANDBOX')
        UUIDGEN = uuid.uuid4()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + CIRCLEAPIKEY
        }



        creditCardTotal = request.POST.get('creditCardTotal')
        print(creditCardTotal)
        creditCardEncrypted = request.POST.get('creditCardEncrypted')
        creditCardName = request.POST.get('creditCardName')
        creditCardDate = request.POST.get('creditCardDate')
        billingLine1 = request.POST.get('billingLine1')
        billingLine2 = request.POST.get('billingLine2')
        billingCountry = request.POST.get('billingCountry')
        billingdistrict = request.POST.get('billingdistrict')
        billingCity = request.POST.get('billingCity')
        billingZip = request.POST.get('billingZip')

        print(creditCardEncrypted)

        creditCardDateYYYY = int('20' + creditCardDate[-2:])
        creditCardDateMM = int(creditCardDate[:2])
        print(creditCardDateMM)
        print(creditCardDateYYYY)

        keyid = 'key1'
        sessionId = 'xxx'
        ipAddress = '172.33.222.1'
        email = 'customer-0001@circle.com'
        phoneNumber = '+12025550180'

        payloadCard = {
            "idempotencyKey": str(UUIDGEN),
            "expMonth": creditCardDateMM,
            "expYear": creditCardDateYYYY,
            "keyId": keyid,
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
                "email": email,
                "phoneNumber": phoneNumber,
                "sessionId": sessionId,
                "ipAddress": ipAddress
            }
        }

        try:
            urlCard = "https://api-sandbox.circle.com/v1/cards"
            responseCard = requests.post(urlCard, json=payloadCard, headers=headers)
            responseCardJson = responseCard.json()

            print(responseCardJson)

            if responseCardJson['data']:
                print('Card Created')
                print(responseCardJson)

                if responseCardJson['data']['network'] == 'VISA':
                    cardflag = 0
                else:
                    cardflag = 1

                cardnew = card(
                    user=request.user,
                    cardid=responseCardJson['data']['id'],
                    flag=cardflag,
                    last=responseCardJson['data']['last4'],
                )
                cardnew.save()



                payloadtx = {
                    "metadata": {
                        "email": email,
                        "sessionId": sessionId,
                        "ipAddress": ipAddress,
                        "phoneNumber": phoneNumber
                    },
                    "amount": {
                        "amount": str(creditCardTotal),
                        "currency": "USD"
                    },
                    "source": {
                        "type": "card",
                        "id": responseCardJson['data']['id']
                    },
                    "verification": "none",
                    "idempotencyKey": str(UUIDGEN),
                    "keyId": keyid,
                    "description": artworks_get.title
                }

                urlTx = "https://api-sandbox.circle.com/v1/payments"
                responseTx = requests.post(urlTx, json=payloadtx, headers=headers)
                responseTxJson = responseTx.json()
                print(responseTxJson)

                if responseTxJson['data']:
                    print('Transaction Created')


                    txnew = transaction(
                        product=artworks_get,
                        client=request.user,
                        status=3,
                        fiat=artworks_get.fiat,
                        price=creditCardTotal,
                        txid=responseTxJson['data']['id'],
                        gateway=1,
                    )
                    txnew.save()

                    artworks_get.sold = True
                    artworks_get.save()

                    return redirect('transaction-detail', txnew.id)

                else:
                    print('Error - Transaction')
                    print(responseTxJson['code'])

            else:
                print('Error - Creation Card')
                print(responseCardJson['code'])

        except requests.exceptions.RequestException as e:
            print(e)

    context['product'] = artworks_get
    context['page'] = 'checkout'

    if artworks_get.sold == True:
        return redirect('artworks-detail', pk)
    else:
        return render(request, 'art/checkout.html', context)

class pagegallerydetail(DetailView):
    model = gallery
    template_name = 'art/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def pageartistdetail(request, slug):
    context = {}
    artist = UserAccount.objects.get(nickname=slug)
    context['artist'] = artist
    get_artwork = product.objects.filter(artist=artist)
    context['artworks'] = get_artwork

    return render(request, 'art/artist.html', context)


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
    context['page'] = 'mint'
    return render(request, 'art/mint.html', context)

def productminttokensol(request):

    if request.method == 'POST':

        print('start Minting')

        context = {}
        data = json.loads(request.body)
        artworks_get = product.objects.get(pk=data['pk'])

        if not artworks_get.mintinghash:

            account = Account(settings.KEYPAIR[:32])
            cfg = {
                "PRIVATE_KEY": base58.b58encode(account.secret_key()).decode("ascii"),
                "PUBLIC_KEY": str(account.public_key()),
                "DECRYPTION_KEY": Fernet.generate_key().decode("ascii")
            }
            metaplex_api = MetaplexAPI(cfg)

            try:
                deploy = metaplex_api.deploy(settings.SOL_ENDPOINT, "Artyste_", "ART")

                artworks_get.mintinghash = deploy
                artworks_get.save()

                context['status'] = '200'
                context['token'] = deploy
                return JsonResponse(context)
            except:
                context['status'] = '400'
                return JsonResponse(context)
        else:
            context['status'] = '200'
            context['token'] = artworks_get.mintinghash
            return JsonResponse(context)

def productmintmetasol(request):

    if request.method == 'POST':

        print('start NFT')
        context = {}
        data = json.loads(request.body)
        artworks_get = product.objects.get(pk=data['pk'])

        print(data['metadata'])

        account = Account(settings.KEYPAIR[:32])
        cfg = {
            "PRIVATE_KEY": base58.b58encode(account.secret_key()).decode("ascii"),
            "PUBLIC_KEY": str(account.public_key()),
            "DECRYPTION_KEY": Fernet.generate_key().decode("ascii")
        }
        metaplex_api = MetaplexAPI(cfg)

        if data['sing_account']:
            sing_account = data['sing_account']
        else:
            sing_account = "5qZ3aah17jwNVf8MLQKKQWV5w3vAkTNZmyu6ex8eJpHK"

        try:
            nft = metaplex_api.mint(settings.SOL_ENDPOINT, artworks_get.mintinghash, sing_account, data['metadata'])

            artworks_get.mintingstatus = 2
            artworks_get.save()

            context['status'] = '200'
            context['nft'] = nft
            return JsonResponse(context)

        except:
            context['status'] = '400'
            return JsonResponse(context)

def pagetxdetail(request, pk):
    context = {}
    print(pk)
    tx_get = transaction.objects.get(pk=pk)

    if tx_get.status == 3:
        CIRCLEAPIKEY = os.getenv('ARTYSTEDEMO_CIRCLE_SANDBOX')
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + CIRCLEAPIKEY
        }

        urltx = "https://api-sandbox.circle.com/v1/payments/" + tx_get.txid
        responseTx = requests.get(urltx, headers=headers)
        responseTxJson = responseTx.json()
        if responseTxJson['data']:

            if responseTxJson['data']['status'] == 'confirmed':
                tx_get.status = 1
                tx_get.product.owner = tx_get.client
                tx_get.save()
                tx_get.product.save()

    context['transaction'] = tx_get
    context['page'] = 'transaction-details'
    return render(request, 'art/transaction-detail.html', context)
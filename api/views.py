from django.shortcuts import render
from django.http import JsonResponse
from .serializers import gallerySerializers, productSerializers, userSerializers
from rest_framework.response import Response
from art.models import gallery, product, nft
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from accounts.models import UserAccount

# Create your views here.
def apiEndPoint(requests):

    apiendpoint = {}
    apiendpoint['Galleries List'] = 'galleries-list/'
    apiendpoint['Galery Detail'] = 'gallery/<slug:slug>/'

    return JsonResponse(apiendpoint, safe=False)# Create your views here.

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apiGalleriesList(requests):
    gallery_get = gallery.objects.all()
    serializer = gallerySerializers(gallery_get, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apiGalleryDetail(requests, slug):
    gallery_get = gallery.objects.get(slug=slug)
    artwork_get = product.objects.filter(gallery=gallery_get)
    serializer = productSerializers(artwork_get, many=True)
    new_serializer_data = list(serializer.data)
    new_serializer_data.append({'gallery': {
        'name': gallery_get.name,
        'avatar': gallery_get.imglogo.url,
        'banner': gallery_get.imgbabner.url,
        'description': gallery_get.description,
        'virtual': gallery_get.virtual.id,
    }})
    return Response(new_serializer_data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apiAssetsList(requests):
    artwork_get = product.objects.all().order_by('created_at').reverse()
    serializer = productSerializers(artwork_get, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apiAsset(requests, pk):
    artwork_get = product.objects.filter(pk=pk)
    serializer = productSerializers(artwork_get, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apiUser(requests, pk):
    user_get = UserAccount.objects.filter(pk=pk)
    serializer = userSerializers(user_get, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def apinft(request):

    Status = {}

    nft_get = request.data
    nft_get_nft = nft_get['nft']
    nft_get_sale = nft_get['sale']
    nft_get_status = nft_get['status']
    nft_get_wallet = nft_get['wallet']

    newnft = nft(
        nft=nft_get_nft,
        sale=1,
        status=1,
        wallet=nft_get_wallet,
    )
    newnft.save()

    Status['nft'] = True
    return JsonResponse(Status, safe=False)
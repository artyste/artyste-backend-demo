from django.shortcuts import render
from django.http import JsonResponse
from .serializers import gallerySerializers, productSerializers
from rest_framework.response import Response
from art.models import gallery, product
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
def apiEndPoint(requests):
    return JsonResponse('API EndPoint', safe=False)# Create your views here.

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
    }})
    return Response(new_serializer_data)
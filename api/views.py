from django.shortcuts import render
from django.http import JsonResponse
from .serializers import gallerySerializers, productSerializers
from rest_framework.response import Response
from art.models import gallery, product
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
def apiEndPoint(requests):
    return JsonResponse('API EndPoint', safe=False)# Create your views here.

def apiGalleryList(requests):
    return JsonResponse('Gallery List', safe=False)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def apiGalleryDetail(requests, slug):
    gallery_get = gallery.objects.get(slug=slug)
    artwork_get = product.objects.filter(gallery=gallery_get)
    serializer = productSerializers(artwork_get, many=True)
    return Response(serializer.data)
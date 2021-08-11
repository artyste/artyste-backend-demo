from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def apiEndPoint(requests):
    return JsonResponse('API EndPoint', safe=False)# Create your views here.

def apiGalleryList(requests):
    return JsonResponse('Gallery List', safe=False)

def apiGalleryDetail(requests):
    return JsonResponse('Gallery Detail', safe=False)
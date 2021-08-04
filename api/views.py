from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def apiEndPoint(requests):
    return JsonResponse('API EndPoint', safe=False)
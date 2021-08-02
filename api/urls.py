from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiEndPoint, name='api-end-point'),
]
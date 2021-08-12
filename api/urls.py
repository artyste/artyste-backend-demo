from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiEndPoint, name='api-end-point'),
    path('gallery-list/', views.apiGalleryList, name='api-gallery-list'),
    path('gallery/<slug:slug>/', views.apiGalleryDetail, name='api-gallery'),
]
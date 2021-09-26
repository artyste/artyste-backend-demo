from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiEndPoint, name='api-end-point'),
    path('galleries-list/', views.apiGalleriesList, name='api-galleries-list'),
    path('gallery/<slug:slug>/', views.apiGalleryDetail, name='api-gallery'),
]
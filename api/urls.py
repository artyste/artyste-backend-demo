from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiEndPoint, name='api-end-point'),
    path('assets-list/', views.apiAssetsList, name='api-assets-list'),
    path('asset/<int:pk>/', views.apiAsset, name='api-asset'),
    path('galleries-list/', views.apiGalleriesList, name='api-galleries-list'),
    path('gallery/<slug:slug>/', views.apiGalleryDetail, name='api-gallery'),
]
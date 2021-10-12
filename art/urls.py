from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.pagehome, name='home'),
    path('artworks/', views.pageartworks, name='artworks'),
    path('artworks/new', views.pageartworksnew, name='artworks-new'),
    path('artworks/<int:pk>/', views.pageproductdetail, name='artworks-detail'),
    path('artworks/checkout/<int:pk>/', views.pagecheckout, name='checkout'),
    path('artworks/mint/<int:pk>/', views.pageproductmint, name='artworks-mint'),
    path('artworks/mint/sol/token/', views.productminttokensol, name='artworks-mint-token-sol'),
    path('artworks/mint/sol/metadata/', views.productmintmetasol, name='artworks-mint-metadata-sol'),
    path('gallery/<slug:slug>/', views.pagegallerydetail.as_view(), name='gallery-detail'),
    path('galleries/', views.pagegalleries, name='galleries'),
    path('transactions/<int:pk>/', views.pagetxdetail, name='transaction-detail'),
]
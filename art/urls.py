from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.pagehome, name='home'),
    path('artworks/', views.pageartworks, name='artworks'),
    path('artworks/new', views.pageartworksnew, name='artworks-new'),
]
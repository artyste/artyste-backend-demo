from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registeruser, name='register'),
    path('profile/wallet', views.profilewallet, name='profile-wallet'),
]
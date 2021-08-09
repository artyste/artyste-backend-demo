from django.shortcuts import render, redirect, reverse
from .form import LoginCustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, authenticated_user

# Create your views here.
@unauthenticated_user
def loginuser(request):
    form = LoginCustomUserForm()
    context = {'form': form}

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:

            login(request, user)
            return redirect('home')

        else:
            messages.warning(request, 'The user name or password is incorrect!')
            return render(request, 'accounts/login.html', context)

    return render(request, 'accounts/login.html', context)

def registeruser(request):
    pass

def logoutUser(request):
    logout(request)
    return redirect('home')
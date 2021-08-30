from django.shortcuts import render, redirect, reverse
from .form import LoginCustomUserForm, CreateCustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, authenticated_user
from .models import card

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
    form = CreateCustomUserForm()


    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CreateCustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}


    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def profilewallet(request):
    context = {}
    context['profile'] = request.user
    context['cards'] = card.objects.filter(user=request.user)


    return render(request, 'accounts/profile-wallet.html', context)

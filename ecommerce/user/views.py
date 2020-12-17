from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Customer
from .decorators import *
from store.utils import *


@unauthenticated_user
def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('store')
        else:
            return render(request, 'user/login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)


@unauthenticated_user
def register_view(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            Customer.objects.create(user=user)
            login(request, user)
            return redirect('store')
        else:
            context = {
                'form': form,
            }
            return render(request, 'user/register.html', context)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

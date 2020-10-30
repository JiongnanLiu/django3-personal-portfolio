from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import StockScreenerForm
from .models import StockScreener, StockPrice
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from portfolio import views
from mysite import urls
from .stock import Stock
from django.http import JsonResponse
import pandas as pd


# Create your views here.


# def stockscreener(request):
# return render(request, 'stockscreener/stockscreener.html')


def userSignup(request):

    if request.method == "GET":
        return render(request, 'stockscreener/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('stockscreener')
            except:
                return render(request, 'stockscreener/signup.html', {'form': UserCreationForm(), 'error': 'Username has already been taken. Please choose a new username.'})

        else:
            return render(request, 'stockscreener/signup.html', {'form': UserCreationForm(), 'error': 'Passwords did not match.'})


@login_required
def userLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('stockscreener')


def userLogin(request):
    if request.method == "GET":
        return render(request, 'stockscreener/signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if not user:
            return render(request, 'stockscreener/signin.html', {'form': AuthenticationForm(), 'error': 'username not found or password does not match.'})
        else:
            login(request, user)
            return redirect('stockscreener')


def stockscreener(request):
    sp500 = Stock()
    table = sp500.get_sp500_comp_last_price()
    print(table)
    return render(request, 'stockscreener/stockscreener.html', {'stock_data': table})

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from store import *

# Create your views here.
from login.forms import RegisterForm


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect('store')
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {'form': form})

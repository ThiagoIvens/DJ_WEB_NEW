from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from login.forms import RegisterForm
from django.contrib import messages
from store import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            messages.success(request, f"Novo usuario criado: {username}")

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
        for msg in form.error_messages:
            messages.error(request, f"{msg}: {form.error_messages[msg]}")

    return render(request, 'registration/register.html', {'form': form})

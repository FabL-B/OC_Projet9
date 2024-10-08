from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm


def index(request):
    """Sign in page."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('flux:flux')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flux:flux')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def logout_user(request):
    """Logout connected user."""
    logout(request)
    return redirect('accounts:login')

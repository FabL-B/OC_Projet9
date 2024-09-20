from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import AppUserCreationForm

def signup(request):
    if request.method == 'POST':
            form = AppUserCreationForm(request.POST)
            if form.is_valid():
                form.save()  # Enregistre le nouvel utilisateur
                return redirect(reverse_lazy('login'))  # Redirige vers la page de connexion
    else:
        form = AppUserCreationForm()
        
    return render(request, 'authentication/signup.html', {'form': form})    

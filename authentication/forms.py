from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser

class AppUserCreationForm(UserCreationForm):
    
    class Meta:
        model = AppUser
        fields = ('username',)
    
    password1 = forms.CharField(
        label = 'password',
         widget=forms.PasswordInput(),
    )
    
    password2 = forms.CharField(
        label="confirm password",
        widget=forms.PasswordInput(),
        help_text="Enter same password as previously",
    )
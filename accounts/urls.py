"""Defines URL patterns for accounts."""

from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    # Index page
    path('', views.index, name='index'),
    # Registration page
    path('signup/', views.signup, name='signup'),
    # User home page
    path('home/', views.home, name='home'),
    # Logout
    path('logout/', views.logout_user, name='logout'),
]
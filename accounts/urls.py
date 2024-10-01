"""Defines URL patterns for accounts."""

from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    # Index page
    path('', views.index, name='login'),
    # Registration page
    path('signup/', views.signup, name='signup'),
    # Logout
    path('logout/', views.logout_user, name='logout'),
]
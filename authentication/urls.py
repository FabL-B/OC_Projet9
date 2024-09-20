"""Defines URL patterns for authentication."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
"""Defines URL patterns for reviews."""

from django.urls import path

from . import views

app_name = 'flux'
urlpatterns = [
        # Page that shows all tickets and reviews from user and follow users(Flux)
    path("", views.flux, name="flux"),
]


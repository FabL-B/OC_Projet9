"""Defines URL patterns for reviews."""

from django.urls import path

from . import views

app_name = "flux"
urlpatterns = [
    # Page that shows all tickets and reviews from user and follow users(Flux)
    path("", views.flux, name="flux"),
    # Page that shows only tickets and reviews from user
    path("posts/", views.posts, name="posts"),
    # Page that shows posts from a specific user
    path("posts/<int:user_id>/", views.posts, name="user_posts"),
]

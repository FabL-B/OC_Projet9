"""Defines URL patterns for reviews."""

from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    # Page that shows all tickets and reviews from user and follow users(Flux)
    #path("reviews/flux/", views.flux(), name="flux"),
    # Page that shows all tickets from a user(Posts)
    path('reviews/posts/', views.posts, name='posts'),
    # Page to handle user subsriptions
    path("reviews/subscriptions/", views.subscriptions, name="subscriptions"),
    # Page to create a new ticket
    path('reviews/new_ticket/', views.new_ticket, name='new_ticket'),
    # Detail page for a single ticket
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]
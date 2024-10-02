"""Defines URL patterns for reviews."""

from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    # Page that shows all tickets from a user(Posts)
    path('posts/', views.posts, name='posts'),
    # Page to handle user subsriptions
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    # Page to create a new ticket
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    # Detail page for a single ticket
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    # Page to create a new review and ticket
    path('new_review/', views.new_review, name='new_review'),
    # Page to create a new review from existing ticket
    path('new_review/<int:ticket_id>/', views.new_review, name='new_review_for_ticket'),
]
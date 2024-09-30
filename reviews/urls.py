"""Defines URL patterns for reviews."""

from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    # Page to create a new ticket
    path('reviews/new_ticket/', views.new_ticket, name='new_ticket'),
    # Page that shows all tickets from a user
    path('reviews/tickets', views.tickets, name='tickets'),
    # Detail page for a single ticket
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]
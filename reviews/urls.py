"""Defines URL patterns for reviews."""

from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    # Page to create a new ticket
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    # Page for editing a ticket
    path('edit_ticket/:<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    # Page to delete a ticket
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    # Page to create a new review and new ticket
    path('new_review/', views.new_review, name='new_review'),
    # Page to create a new review from existing ticket
    path('new_review/<int:ticket_id>/', views.new_review, name='new_review_for_ticket'),
    # Page for editing a review
    path('edit_review/:<int:review_id>/', views.edit_review, name='edit_review'),
    # Page to delete a review
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]
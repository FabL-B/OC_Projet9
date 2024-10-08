"""Defines URL patterns for subscriptions."""

from django.urls import path

from . import views

app_name = 'subscriptions'
urlpatterns = [
    # Page that handle user search, followers, and following
    path('', views.manage_subscriptions, name='subscriptions'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:followed_user_id>/', views.unfollow, name='unfollow'),
]

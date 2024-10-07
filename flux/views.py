from itertools import chain

from django.db.models import CharField, Value
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from reviews.models import Ticket, Review
from subscriptions.models import UserFollows
from accounts.models import CustomUser


@login_required
def flux(request):
    """Show reviews and tickets from connected user and followed users."""

    # Get reviews from connected and followed users
    reviews = get_user_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    # Get tickets from connected and followed users
    tickets = get_user_viewable_tickets(request.user)
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    # Check if each ticket has an associated review
    for ticket in tickets:
        ticket.has_review = Review.objects.filter(ticket=ticket).exists()

    # Combine and sort posts (tickets and reviews)
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    context = {"posts": posts}
    return render(request, "flux/flux.html", context)


def get_user_viewable_reviews(user):
    """Get a queryset of reviews viewable by connected user"""

    # Get followed users
    followed_users = UserFollows.objects.filter(
        user=user).values_list('followed_user', flat=True)

    # Get reviews from followed users and the connected user
    reviews_from_followed = Review.objects.filter(
        user__in=[user.id] + list(followed_users))

    # Get reviews on tickets created by the connected user
    reviews_on_user_tickets = Review.objects.filter(ticket__user=user)

    # Combine reviews into a single queryset using union
    viewable_reviews = reviews_from_followed | reviews_on_user_tickets
    # Remove duplicates from reviews_on_user_tickets
    viewable_reviews = viewable_reviews.distinct()

    return viewable_reviews


def get_user_viewable_tickets(user):
    """Get a queryset of tickets viewable by connected user"""

    # Get followed users
    followed_users = UserFollows.objects.filter(
        user=user).values_list('followed_user', flat=True)

    # Get tickets from followed users and the connected user
    viewable_tickets = Ticket.objects.filter(
        user__in=[user.id] + list(followed_users))

    return viewable_tickets


@login_required
def posts(request, user_id=None):
    """Show only reviews and tickets from connected user or selected user."""

    if user_id:
        user = CustomUser.objects.get(id=user_id)
    else:
        user = request.user

    # Get reviews from connected and followed users
    user_reviews = Review.objects.filter(user=user)
    user_reviews = user_reviews.annotate(
        content_type=Value("REVIEW", CharField()))
    # Get tickets from connected and followed users
    user_tickets = Ticket.objects.filter(user=user)
    user_tickets = user_tickets.annotate(
        content_type=Value("TICKET", CharField()))

    posts = sorted(
        chain(user_reviews, user_tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )

    context = {
        "posts": posts,
        "user_profile": user,
    }
    return render(request, "flux/posts.html", context)

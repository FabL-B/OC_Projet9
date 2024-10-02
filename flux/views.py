from itertools import chain

from django.db.models import CharField, Value
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from reviews.models import Ticket, Review, UserFollows
from reviews.forms import TicketForm, ReviewForm
from accounts.models import CustomUser


@login_required
def flux(request):
    """Show reviews and tickets from connected user and followed users."""
    
    # Get followed users
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)
    # Get reviews from connected and followed users
    reviews = Review.objects.filter(user__in=[request.user.id] + list(followed_users))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    # Get tickets from connected and followed users
    tickets = Ticket.objects.filter(user__in=[request.user.id] + list(followed_users))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    # Combine and sort posts (tickets and reviews)
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    context = {'posts': posts}
    return render(request, 'flux/flux.html', context)

@login_required
def posts(request):
    """Show only reviews and tickets from connected user."""
    # Récupérer tous les tickets et reviews de l'utilisateur connecté
    user_tickets = Ticket.objects.filter(user=request.user).order_by('-time_created')
    user_reviews = Review.objects.filter(user=request.user).order_by('-time_created')
    
    context = {'tickets': user_tickets,
               'reviews': user_reviews,
               }
    return render(request, 'flux/posts.html', context)
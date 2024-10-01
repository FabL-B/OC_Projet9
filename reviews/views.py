from itertools import chain

from django.db.models import CharField, Value
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Ticket, Review, UserFollows
from .forms import TicketForm, ReviewForm
from accounts.models import CustomUser


@login_required
def posts(request):
    """Show all tickets from connected user."""
    tickets = Ticket.objects.filter(user=request.user).order_by('time_created')
    context = {'tickets': tickets}
    return render(request, 'reviews/posts.html', context)

@login_required
def subscriptions(request):
    """Show all followed users and search for new users."""
    followed_users = UserFollows.objects.filter(user=request.user)
    context = {'followed_users': followed_users}
    return render(request, 'reviews/subscriptions.html', context)

@login_required
def new_ticket(request):
    """Add a new ticket."""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TicketForm()
    else:
        # POST data subimtted; process data
        form = TicketForm(data=request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            return redirect('reviews:posts')

    context = {'form': form}
    return render(request, 'reviews/new_ticket.html', context)

@login_required
def ticket_detail(request, ticket_id):
    """Show a single ticket and it's review."""
    ticket = Ticket.objects.get(id=ticket_id)
    
    # Check if ticket already have a review
    existing_review = Review.objects.filter(ticket=ticket)
    
    if existing_review:
        context = {'ticket': ticket,'existing_review': existing_review}
        return render(request, 'reviews/ticket_detail.html', context)
    
    
    if request.method == 'POST':
         # POST data submitted; process data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.ticket = ticket 
            new_review.user = request.user
            new_review.save()
            return redirect('reviews:ticket_detail', ticket_id=ticket.id)
    else:
        # No data submitted; creat a blank form
        form = ReviewForm()

    # Display a blank fomr or existing review
    context = {'ticket': ticket, 'form': form}
    return render(request, 'reviews/ticket_detail.html', context)

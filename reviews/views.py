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
def edit_ticket(request, ticket_id):
    pass

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

@login_required
def new_review(request, ticket_id=None):
    """Create a review from an existing or new ticket"""
    
    ticket = None
    if ticket_id:
        ticket = Ticket.objects.get(id=ticket_id)
    
    if request.method == 'POST':
        # POST data submitted; process data
        review_form = ReviewForm(request.POST)
        
        # If ticket exist, ticket form is prefilled
        if ticket:
            ticket_form = TicketForm(instance=ticket)
        # Else create empty ticket form
        else:
            ticket_form = TicketForm(request.POST, request.FILES)
            
        if review_form.is_valid() and (not ticket or ticket_form.is_valid()):

            if not ticket:
                new_ticket = ticket_form.save(commit=False)
                new_ticket.user = request.user
                new_ticket.save()
            else:
                new_ticket = ticket
            
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.ticket = new_ticket
            new_review.save()
    
            return redirect('flux:flux')
     
    else:
        # Make the ticket form read-only if it already exists
        if ticket:
            ticket_form = TicketForm(instance=ticket)
            review_form = ReviewForm()
            for field in ticket_form.fields:
                ticket_form.fields[field].widget.attrs['readonly'] = True

        else:
            # Empty forms for creating a new ticket and review
            ticket_form = TicketForm()
            review_form = ReviewForm()

    return render(request, 'reviews/new_review.html', {
        'ticket_form': ticket_form,
        'review_form': review_form,
        'ticket': ticket
    })

@login_required
def edit_review(request, review_id):
    pass
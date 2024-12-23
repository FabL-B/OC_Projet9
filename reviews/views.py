from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Ticket, Review
from .forms import TicketForm, ReviewForm


@login_required
def new_ticket(request):
    """Add a new ticket."""
    if request.method != "POST":
        # No data submitted; create a blank form
        ticket_form = TicketForm()
    else:
        # POST data subimtted; process data
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            return redirect("flux:flux")

    context = {"ticket_form": ticket_form}
    return render(request, "reviews/new_ticket.html", context)


@login_required
def edit_ticket(request, ticket_id):
    """Edit a ticket."""
    # Get the ticket to edit from the ID in the URL
    ticket = Ticket.objects.get(id=ticket_id, user=request.user)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("flux:posts")
    else:
        form = TicketForm(instance=ticket)

    context = {"form": form, "ticket": ticket}
    return render(request, "reviews/edit_ticket.html", context)


@login_required
def delete_ticket(request, ticket_id):
    """Delete a ticket."""
    # Get the ticket to delete from the ID in the URL
    ticket = Ticket.objects.get(id=ticket_id, user=request.user)
    if request.method == "POST":
        ticket.delete()
        return redirect("flux:posts")

    context = {"ticket": ticket}
    return render(request, "reviews/delete_ticket.html", context)


@login_required
def new_review(request, ticket_id=None):
    """Create a review from an existing or new ticket"""
    ticket = None
    if ticket_id:
        ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        # If ticket exist, ticket form is prefilled
        if ticket:
            ticket_form = TicketForm(instance=ticket)
        # Else create empty ticket form
        else:
            ticket_form = TicketForm(request.POST, request.FILES)

        if review_form.is_valid() and (ticket or ticket_form.is_valid()):

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

            return redirect("flux:flux")

    else:
        # Make the ticket form read-only if it already exists
        if ticket:
            ticket_form = TicketForm(instance=ticket)
            review_form = ReviewForm()
            for field in ticket_form.fields:
                ticket_form.fields[field].widget.attrs["readonly"] = True

        else:
            # Empty forms for creating a new ticket and review
            ticket_form = TicketForm()
            review_form = ReviewForm()

    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
        "ticket": ticket
    }
    return render(request, "reviews/new_review.html", context)


@login_required
def edit_review(request, review_id):
    """Edit a review"""
    # Get the review to edit from the ID in the URL
    review = Review.objects.get(id=review_id, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("flux:posts")
    else:
        form = ReviewForm(instance=review)

    context = {"form": form, "review": review}
    return render(request, "reviews/edit_review.html", context)


@login_required
def delete_review(request, review_id):
    """Delete a review."""
    # Get the review to delete from the ID in the URL
    review = Review.objects.get(id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect("flux:posts")

    context = {"review": review}
    return render(request, "reviews/delete_review.html", context)

from django import forms

from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    """A form to create a ticket."""
    class Meta:
        model = Ticket
        exclude = ('user', 'time_created')
        
class ReviewForm(forms.ModelForm):
    """A form to create a review."""
    class Meta:
        model = Review
        exclude = ('user', 'time_created', 'ticket')
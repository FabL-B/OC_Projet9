from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import CustomUser
from LITReview import settings


class Ticket(models.Model):
    """A topic from a user."""
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='ticket_img/', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.title


class Review(models.Model):
    """A review from a user."""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.headline[:50]}..."

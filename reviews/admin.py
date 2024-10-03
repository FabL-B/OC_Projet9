from django.contrib import admin

from .models import Ticket, Review

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'user')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)

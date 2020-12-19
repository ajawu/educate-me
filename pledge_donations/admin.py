from django.contrib import admin
from .models import Donations, Subscription, Books, Contact, Event


@admin.register(Donations)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor', 'amount', 'donation_time']
    list_filter = ['donation_time', 'amount']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'contact_email', 'message_title']
    list_filter = ['has_reached_out']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_joined']
    list_filter = ['date_joined', 'email']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'publisher', 'total_donated']
    list_filter = ['name', 'total_donated']


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'event_time', 'donation_amount', 'venue_state',
                    'venue_street_address']
    list_filter = ['donation_amount', 'event_time']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

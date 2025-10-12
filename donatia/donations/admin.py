from django.contrib import admin
from .models import Donation

# Register your models here.
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'cause', 'amount', 'payment_method', 'status', 'donated_at')
    list_filter = ('status', 'payment_method', 'donated_at')
    search_fields = ('donor__email', 'cause__title', 'transaction_id')
    ordering = ('-donated_at',)

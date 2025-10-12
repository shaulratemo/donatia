from django.contrib import admin
from .models import Cause

# Register your models here.
@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'target_amount', 'raised_amount', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description', 'organization__name')
    ordering = ('-created_at',)

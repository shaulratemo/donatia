from django.contrib import admin
from .models import Organization

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website', 'status', 'user', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'description', 'website')
    ordering = ('-created_at',)

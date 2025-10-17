from django.db import models
from organizations.models import Organization
from decimal import Decimal


class Cause(models.Model):
    """
    Represents a fundraising cause created by an Organization.
    Only active causes are shown publicly.
    """
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='causes'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    raised_amount = models.DecimalField(
        max_digits=12, decimal_places=2,
        default=Decimal('0.00')
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.organization.name})"

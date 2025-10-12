from django.db import models
from django.conf import settings
from causes.models import Cause
from decimal import Decimal

# Create your models here.
class Donation(models.Model):
    """
    Represents a donation made by a donor to a cause.
    """
    PAYMENT_METHOD_CHOICES = [
        ('MPESA', 'M-PESA'),
        ('CARD', 'Card'),
        ('BANK', 'Bank Transfer'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='donations'
    )
    cause = models.ForeignKey(
        Cause,
        on_delete=models.CASCADE,
        related_name='donations'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='successful')
    donated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-donated_at']

    def __str__(self):
        return f"{self.donor.email} → {self.cause.title} ({self.amount})"

    def save(self, *args, **kwargs):
        """Automatically update cause's raised amount if successful."""
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new and self.status == 'successful':
            self.cause.raised_amount += Decimal(self.amount)
            self.cause.save()

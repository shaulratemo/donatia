from django.db import models
from django.conf import settings

# Create your models here.
class Organization(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    # The user who owns/registered this organization
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organization'
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    website = models.URLField(max_length=300, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"

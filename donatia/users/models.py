from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

# Create your models here.
# Custom User Manager
class UserManager(BaseUserManager):
    """Manager for custom User model with email as username."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required for registration.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with admin role."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")

        if not password:
            raise ValueError("Superusers must have a password.")

        return self.create_user(email, password, **extra_fields)


# User Roles Enum
class UserRoles(models.TextChoices):
    DONOR = "donor", "Donor"
    ORGANIZATION = "organization", "Organization"
    ADMIN = "admin", "Admin"


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.DONOR)

    is_active = models.BooleanField(default=True) # Required by Django
    is_staff = models.BooleanField(default=False) # For superusers (Admins)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ({self.role})"

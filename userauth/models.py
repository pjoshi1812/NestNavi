from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)  # Email is now used for authentication
    username = models.CharField(max_length=100, unique=True)  # Optional
    ROLE_CHOICES = [
        ('user', 'User'),
        ('owner', 'Owner'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'  # Email will be the field used for login
    REQUIRED_FIELDS = ['username']  # Username is required for superuser creation

    def __str__(self):
        return f"{self.email} ({self.role})"

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Guest', 'Guest'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return self.username

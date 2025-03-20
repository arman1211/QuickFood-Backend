from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("user", "User"),
        ("restaurant_owner", "Restaurant Owner"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")

from django.db import models
from users.models import CustomUser


class Restaurant(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="restaurant",
    )
    image = models.ImageField(upload_to="restaurant/", null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("Salad", "Salad"),
        ("Rolls", "Rolls"),
        ("Deserts", "Deserts"),
        ("Sandwich", "Sandwich"),
        ("Cake", "Cake"),
        ("Pure Veg", "Pure Veg"),
        ("Pasta", "Pasta"),
        ("Noodles", "Noodles"),
        ("Biriyani", "Biriyani"),
        ("Kacchi", "Kacchi"),
    ]

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menu_items"
    )
    image = models.ImageField(upload_to="menu_images/", null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="Salad"
    )

    def __str__(self):
        return f"{self.name} ({self.category})"

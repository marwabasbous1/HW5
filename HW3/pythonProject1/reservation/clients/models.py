from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Food', 'Food'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
        ('Hardware', 'Hardware'),
    ])
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
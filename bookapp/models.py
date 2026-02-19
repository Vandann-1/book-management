from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8,decimal_places=3, default=0.00)
    published_date = models.DateField()

    def __str__(self):
        return self.title

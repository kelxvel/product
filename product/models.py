from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    slug = models.SlugField(blank = True, unique = True)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    slug = models.SlugField(blank = True, unique = True)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(default = timezone.now)
    modified_at = models.DateTimeField(blank = True, null = True)

    def modify(self):
        self.modified_at = timezone.now()
        self.save()

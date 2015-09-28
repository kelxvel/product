from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    slug = models.SlugField(blank = True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    slug = models.SlugField(blank = True)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(default = timezone.now)
    modified_at = models.DateTimeField(blank = True, null = True)

    def modify(self):
        self.modified_at = timezone.now()
        self.save()
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='listings')
    category = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    modified = models.DateTimeField(auto_now=True)
    

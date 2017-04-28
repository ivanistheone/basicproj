from django.db import models

# Create your models here.

class Restaurant(models.Model):
    # id
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    address3 = models.CharField(max_length=100)
    stars = models.IntegerField()
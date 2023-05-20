from django.db import models


# Create your models here.
class ByersData(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.PositiveIntegerField()

    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    house = models.PositiveIntegerField()
    flat = models.PositiveIntegerField()

    message = models.TextField()  # неограниченной длины, а CharField конечную длину имеет

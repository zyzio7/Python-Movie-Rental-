from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    year = models.CharField(max_length=4, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    rate = models.FloatField(null=True)


class Cart(models.Model):
    movie = models.ManyToManyField(Movie)
    session = models.CharField(max_length=50, null=True)
    total_cost = models.FloatField(default=0)


class Rental(models.Model):
    user = models.ForeignKey(User, null=True)
    cart = models.ForeignKey(Cart, null=True)
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)
    total_cost = models.FloatField(default=0)

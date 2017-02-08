from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)


class Customer(models.Model):
    username = models.CharField(max_length=30)


class Rental(models.Model):
    customer = models.ForeignKey(Customer)
    movie = models.ManyToManyField(Movie)

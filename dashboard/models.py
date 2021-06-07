from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Coin(models.Model):

    class CoinObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() 

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250) 
    objects = models.Manager()  # default manager
    coinobjects = CoinObjects()  # custom manager

    class Meta:
        ordering = ('-price',)

    def __str__(self):
        return self.title
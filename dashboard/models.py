from django.db import models
from django.contrib.auth.models import User

class Coin(models.Model):

    class CoinObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() 

    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250) 
    objects = models.Manager()  # default manager
    coinobjects = CoinObjects()  # custom manager

    class Meta:
        ordering = ('-price',)

    def __str__(self):
        return self.title
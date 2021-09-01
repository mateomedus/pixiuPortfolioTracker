from users.models import BinanceUser
from django.db import models
from django.contrib.auth.models import User

class Coin(models.Model):

    class CoinObjects(models.Manager):
        def create_coin(self, name, price):
            coin = self.create(name=name,price=price)
            return coin

        def get_queryset(self):
            return super().get_queryset() 

    name = models.CharField(max_length=250, primary_key=True)
    price = models.CharField(max_length=250) 
    objects = models.Manager()  # default manager
    coinobjects = CoinObjects()  # custom manager

    class Meta:
        ordering = ('-price',)

    def __str__(self):
        return self.name
        

class Portfolio(models.Model):

    class PorfolioObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() 

    coinName = models.ForeignKey(Coin, on_delete=models.PROTECT)
    userId = models.ForeignKey(BinanceUser, on_delete=models.PROTECT, default=1)
    amount = models.FloatField(max_length=20)
    usdValue = models.FloatField(max_length=20)
    objects = models.Manager()  # default manager
    portfolioobjects = PorfolioObjects()  # custom manager

    class Meta:
        
        def __str__(self):
            return self.id

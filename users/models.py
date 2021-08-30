from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BinanceUser(AbstractUser):
    api_key = models.CharField(max_length=250, default="") 
    api_secret = models.CharField(max_length=250,default="") 
    def __str__(self) -> str:
        return self.email
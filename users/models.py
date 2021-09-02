from django.db import models
from django.contrib.auth.models import AbstractUser
from mirage import fields

class BinanceUser(AbstractUser):
    api_key =  models.CharField(max_length=250)  
    api_secret = fields.EncryptedCharField()
  
    def __str__(self) -> str:
        return self.email



from users.serializers import UserSerializer
from users.models import BinanceUser
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class BinanceUserUpdate(generics.ListCreateAPIView):
    """
    def get(self, request, *args, **kwargs):
        user = BinanceUser.objects.filter()
        return super().get(request, *args, **kwargs)
    """
    queryset = BinanceUser.coinobjects.all()
    serializer_class = UserSerializer

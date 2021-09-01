from users.serializers import UserSerializer
from users.models import BinanceUser
from django.shortcuts import render
from rest_framework import generics


class BinanceUserUpdate(generics.ListCreateAPIView):
    queryset = BinanceUser.objects.all()
    serializer_class = UserSerializer

"""
    def get(self, request, *args, **kwargs):
        user = BinanceUser.objects.filter()
        return super().get(request, *args, **kwargs)
    """
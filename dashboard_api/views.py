from rest_framework import generics
from dashboard.models import Coin, Portfolio
from .serializers import CoinSerializer, PortfolioSerializer

class CoinList(generics.ListCreateAPIView):
    queryset = Coin.coinobjects.all()
    serializer_class = CoinSerializer

class CoinDetail(generics.RetrieveDestroyAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer

class PortfolioList(generics.ListCreateAPIView):
    queryset = Portfolio.portfolioobjects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetail(generics.RetrieveDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""

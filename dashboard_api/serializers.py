from rest_framework import serializers
from dashboard.models import Coin, Portfolio

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price')
        model = Coin

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'coinId', 'amount', 'usdValue')
        model = Portfolio
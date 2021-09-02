from rest_framework import serializers
from dashboard_api.models import Coin, Portfolio

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'price')
        model = Coin

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'coinName', 'amount', 'usdValue')
        model = Portfolio



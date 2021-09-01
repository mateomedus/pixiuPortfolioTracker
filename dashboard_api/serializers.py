from rest_framework import serializers
from dashboard.models import BinanceCredentials, Coin, Portfolio

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'price')
        model = Coin

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'coinName', 'amount', 'usdValue')
        model = Portfolio

class BinanceCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'userId', 'api_key', 'api_secret')
        model = BinanceCredentials

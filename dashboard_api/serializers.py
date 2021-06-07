from rest_framework import serializers
from dashboard.models import Coin

class CoinSerializer(serializers.ModelSelializer):
    class Meta:
        model = Coin
        fields = Coin('id' ,'name', 'price')
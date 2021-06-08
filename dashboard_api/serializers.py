from rest_framework import serializers
from dashboard.models import Coin

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price')
        model = Coin
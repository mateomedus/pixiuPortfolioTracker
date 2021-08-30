from rest_framework.serializers import ModelSerializer
from .models import BinanceUser
class UserSerializer(ModelSerializer):
    class Meta:
        model = BinanceUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff', 'api_key', 'api_secret')
        
from django.urls import include, path
from  .views import BinanceUserUpdate

urlpatterns = [
    path('auth/', include('rest_auth.urls')),    
    path('auth/register/', include('rest_auth.registration.urls')),
    path('binancecred/', BinanceUserUpdate.as_view(), name='listcreate'),
]
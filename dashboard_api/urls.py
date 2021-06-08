from django.urls import path
from .views import CoinList, CoinDetail

app_name = 'dashboard_api'

urlpatterns = [
    path('<int:pk>/', CoinDetail.as_view(), name='detailcreate'),
    path('', CoinList.as_view(), name='listcreate'),
]
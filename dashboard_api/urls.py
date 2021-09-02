from django.urls import path
from .views import  CoinList, CoinDetail, PortfolioDetail, PortfolioList

app_name = 'dashboard_api'

urlpatterns = [
    path('<int:pk>/', CoinDetail.as_view(), name='detailcreate'),
    path('', CoinList.as_view(), name='listcreate'),
    path('<int:pk>/', PortfolioDetail.as_view(), name='detailcreate'),
    path('Portfolio', PortfolioList.as_view(), name='listcreate'),
]
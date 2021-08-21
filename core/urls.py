from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('api/', include('dashboard_api.urls', namespace='dashboard_api')),
    path('api/v1/users/', include('users.urls')),
]

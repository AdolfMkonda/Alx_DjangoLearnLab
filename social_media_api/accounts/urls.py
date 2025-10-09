
from django.urls import path
from django.urls import include

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('token/', include('rest_framework.authtoken.urls')),
]
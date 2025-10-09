from django.shortcuts import render
from rest_framework import viewsets
from .models import user
from .serializers import UserSerializer



# Create your views here.
class loginViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class registerViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer


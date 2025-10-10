from django.shortcuts import render
from rest_framework import viewsets
from .models import user
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token


class loginViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class registerViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

class profileViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class modelViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer


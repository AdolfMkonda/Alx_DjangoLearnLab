from django.db import router
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router.register(r'books_all', BookViewSet, basename='book_all')

class obtain_auth_token(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    router.register(r'auth', obtain_auth_token, basename='auth')
    
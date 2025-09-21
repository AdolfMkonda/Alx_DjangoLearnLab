from django.shortcuts import render
from rest_framework import viewsets
from api_project.api.serializers import BookSerializer
from .models import Book


# Create your views here.
class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
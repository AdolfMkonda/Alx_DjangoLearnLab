from rest_framework import serializers
from .models import Book

class BookSerializer:
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
        

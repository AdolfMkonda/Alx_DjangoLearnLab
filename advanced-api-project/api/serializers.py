from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_year']
    def validate_published_year(self, value):
        if value.year > 2025:
            raise serializers.ValidationError("Published year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']


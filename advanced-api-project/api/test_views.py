from .models import Book
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .serializers import BookSerializer
from django.utils import timezone
from datetime import datetime

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": timezone.now().year
        }
        self.book = Book.objects.create(**self.book_data)
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": timezone.now().year
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, data['title'])

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BookSerializer(self.book)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        updated_data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_year": timezone.now().year
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])

    def test_delete_book(self):
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BookSerializer(Book.objects.all(), many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_book_future_publication_year(self):
        future_year = timezone.now().year + 10
        data = {
            "title": "Future Book",
            "author": "Future Author",
            "publication_year": future_year
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
        self.assertEqual(Book.objects.count(), 1)  # No new book should be created
        self.assertEqual(response.data['publication_year'][0], "Published year cannot be in the future.")

    def test_update_book_future_publication_year(self):
        future_year = timezone.now().year + 10
        updated_data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_year": future_year
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
        self.book.refresh_from_db()
        self.assertNotEqual(self.book.publication_year, future_year)  # Publication year should not be updated
        self.assertEqual(response.data['publication_year'][0], "Published year cannot be in the future.")  


from django.db import router
from django.urls import include, path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
router = DefaultRouter()

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),  # Include the router URLs
]
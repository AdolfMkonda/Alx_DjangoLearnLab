from django import urls
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import listView, DetailView, CreateView, UpdateView, DeleteView
router = DefaultRouter()
router.register(r'books', listView, basename='book-list')
router.register(r'books', DetailView, basename='book-detail')
router.register(r'books', CreateView, basename='book-create')
router.register(r'books', UpdateView, basename='book-update')
router.register(r'books', DeleteView, basename='book-delete')   

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)


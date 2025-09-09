from django.urls import path
from . import views
from .views import list_books

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', loginView.as_view(template_name="")),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),    
]
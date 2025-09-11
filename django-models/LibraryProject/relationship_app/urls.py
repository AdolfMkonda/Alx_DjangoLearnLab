from django.urls import path
from . import views
from .views import list_books, LoginView, LogoutView

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="login.html")),
    path('logout/', LogoutView.as_view(template_name="logout.html")),
    path('register/', views.registerView, name='register'),
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/", views.edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete_book"),
]
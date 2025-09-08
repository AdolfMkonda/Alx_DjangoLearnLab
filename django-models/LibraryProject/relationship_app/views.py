from django.shortcuts import render
from .models import Book, Librarian, Library

# Create your views here.
from django.http import HttpResponse

def list_books(request):
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

class library_DetailView():
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

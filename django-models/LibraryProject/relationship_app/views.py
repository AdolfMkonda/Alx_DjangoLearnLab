from django.shortcuts import render
from .models import Book
from .models import Library

# Create your views here.
from django.http import HttpResponse

def list_books(request):
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

class library_DetailView():
    model = Library
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'library'

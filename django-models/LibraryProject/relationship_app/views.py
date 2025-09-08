from django.shortcuts import render
from .models import Books, Librarian, Library

# Create your views here.
from django.http import HttpResponse

def list_books(request):
    return HttpResponse(Books.objects.all())

class library_DetailView():
    model = Library
    context_object_name = 'library'

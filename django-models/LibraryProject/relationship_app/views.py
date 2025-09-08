from django.shortcuts import render
from .models import Books, Librarian, Library

# Create your views here.
from django.http import HttpResponse

def list_books(request):
    return render(request, 'relationship_app/list_books.html', Books.objects.all())

class library_DetailView():
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

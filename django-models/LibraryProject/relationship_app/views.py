from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




# Create your views here.
from django.http import HttpResponse

def list_books(request):
    return render(request, 'relationship_app/list_books.html', Book.objects.all())

class library_DetailView():
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('relationship_app:list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('relationship_app:login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
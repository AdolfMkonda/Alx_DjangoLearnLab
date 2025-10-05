from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostForm 
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator

# Create your views here.
class register:
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'logged_in.html')
        else:
            form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    
class HomeView:
    def home(request):
        return render(request, 'home.html')

class logged_in_view:
    @login_required
    def logged_in_view(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'logged_in.html', {'posts': posts})

class ListView:
    @login_required
    def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    
class DetailView:
    @login_required
    def post_detail(request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    
class CreateView:
    @login_required
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    
class UpdateView:
    @login_required
    def post_edit(request, pk):
        post = Post.objects.get(pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

class DeleteView:
    @login_required
    def post_delete(request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post_list')



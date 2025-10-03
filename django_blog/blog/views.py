from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required

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


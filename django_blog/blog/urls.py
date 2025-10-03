from django.urls import path
from django.urls import include
from .views import SignUpView, HomeView, logged_in_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', HomeView.home, name='home'),
    path('register/', register.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logged_in/', login_required(views.logged_in_view), name='logged_in'),
]

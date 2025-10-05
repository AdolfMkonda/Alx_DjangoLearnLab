from django.urls import path
from django.urls import include
from .views import SignUpView, HomeView, logged_in_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', HomeView.home, name='home'),
    path('register/', auth_views, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logged_in/', login_required(views.logged_in_view), name='logged_in'),
    path('profile/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/new/', views.post_create, name='post_create'),
]

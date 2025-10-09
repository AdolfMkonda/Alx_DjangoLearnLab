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
    path('posts/new/', views.post_new, name='post_new'), --- IGNORE ---
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'), --- IGNORE ---
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'), --- IGNORE --    
    path('comment/', views.comment_list, name='comment_list'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('comment/new/', views.comment_new, name='comment_new'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment_update'),
    path('comments/<int:pk>/new/', views.comment_create, name='comment_create'),
    path('post/<int:pk>/comments/new/', views.comment_create, name='comment_create'), --- IGNORE --
]

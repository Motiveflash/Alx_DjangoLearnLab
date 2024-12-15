from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Home page for blog (ListView of posts)
    path('', views.PostListView.as_view(), name='post-list'),  # List of posts at root
    path('home/', views.home, name='home'),  # Optional home view, if you want a specific page for home
    
    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Blog Post CRUD Views
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
     path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<int:post_pk>/comments/edit/<int:pk>/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('posts/<int:post_pk>/comments/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

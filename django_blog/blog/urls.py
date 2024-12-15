from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Home page for blog (ListView of posts)
    path('', views.PostListView.as_view(), name='post-list'),  # List of posts at root
    
    path('home/', views.home, name='home'),  
    
    
    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Blog Post CRUD Views
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View single post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create new post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete post
    
    # Comment CRUD Views
    path('post/<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='comment-create'),  # Create comment
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),  # Edit comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),  # Delete comment
    
    path('search/', views.search, name='search'),
    path('tag/<str:tag_name>/', views.tag_filter, name='tag-detail'),
    
    # Add the URL pattern for filtering posts by tags
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),
]

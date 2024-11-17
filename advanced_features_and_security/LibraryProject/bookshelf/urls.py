# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('create/', views.create_book, name='create_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

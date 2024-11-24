# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('create/', views.create_book, name='create-book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit-book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete-book'),
]

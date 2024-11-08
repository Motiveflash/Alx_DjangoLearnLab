from .views import list_books
from .views import LibraryDetailView
from django.urls import path

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library'),
]



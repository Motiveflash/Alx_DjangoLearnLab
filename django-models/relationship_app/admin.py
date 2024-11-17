from django.contrib import admin
from .models import Author, Book, Librarian, Library, UserProfile


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Library)
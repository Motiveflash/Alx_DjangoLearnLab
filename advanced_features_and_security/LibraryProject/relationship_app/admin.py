from django.contrib import admin
from .models import  Librarian, Library, UserProfile

admin.site.register(UserProfile)
admin.site.register(Librarian)
admin.site.register(Library)
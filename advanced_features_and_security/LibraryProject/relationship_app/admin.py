from django.contrib import admin
from .models import Library, Librarian, UserProfile

admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)

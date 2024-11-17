from django.conf import settings
from django.db import models
from bookshelf.models import Book




# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")  # Added related_name for better reverse lookups
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):  # Corrected the `__init__` method to `__str__`
        return self.name


# User Profile Model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile")  # Linked to `CustomUser`
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')

    def __str__(self):  # Corrected the `__init__` method to `__str__`
        return f"{self.user.email}'s profile"

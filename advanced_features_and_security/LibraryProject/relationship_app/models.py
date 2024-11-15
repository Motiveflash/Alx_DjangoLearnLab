from django.db import models
from django.contrib.auth.models import User


# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __init__(self):
        return self.name



class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')

    def __init__(self):
        return f"{self.user.username}'s profile"
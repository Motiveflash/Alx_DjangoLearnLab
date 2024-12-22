from django.db import models
from django.contrib.auth.models import AbstractUser

# CustomUser Model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    
    def __str__(self) -> str:
        return self.username
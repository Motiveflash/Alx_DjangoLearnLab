from django.db import models
from django.contrib.auth.models import User


# Model for tags
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

# Model for blog posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


# Model for comments on blog posts
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # to link comments to users
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}' if self.author else f'Comment on {self.post.title}'

    # Optional: Custom validation to prevent empty comment content
    def clean(self):
        if not self.content.strip():
            raise ValidationError("Content cannot be empty.")

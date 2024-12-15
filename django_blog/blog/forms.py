from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post
from taggit.forms import TagField, TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your comment here...'})
        
class PostForm(forms.ModelForm):
    tags = TagField(required=False) 

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags'] 

    # Define the widgets for each field, including the 'tags' field
    widgets = {
        'tags': TagWidget(),  # Use TagWidget to render the tags field
    }
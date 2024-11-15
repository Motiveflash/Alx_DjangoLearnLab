from django import forms
from .models import UserProfile
from bookshelf.models import Book

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["role"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
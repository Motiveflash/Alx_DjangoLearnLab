from rest_framework import serializers 
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Book
        fields = '__all__'
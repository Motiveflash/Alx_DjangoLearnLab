from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookGenericAPIViewTest(TestCase):
    def setUp(self):
        # Create test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')
        
        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')
        
        # Create books
        Book.objects.create(title='Book One', publication_year=2020, author=self.author1)
        Book.objects.create(title='Book Two', publication_year=2021, author=self.author1)
        Book.objects.create(title='Book Three', publication_year=2020, author=self.author2)
        
        # API URL
        self.url = '/api/books/'  # Replace with the actual URL for BookGenericAPIView

    def test_filter_by_publication_year(self):
        response = self.client.get(self.url, {'publication_year': 2020})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Two books with publication_year=2020

    def test_filter_by_author_name(self):
        response = self.client.get(self.url, {'author__name': 'Author One'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Two books by Author One

    def test_combined_filters(self):
        response = self.client.get(self.url, {'publication_year': 2020, 'author__name': 'Author Two'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # One book matches both filters

    def test_invalid_filter_field(self):
        response = self.client.get(self.url, {'nonexistent_field': 'value'})
        self.assertEqual(response.status_code, 400)  # Invalid filter field

    def test_invalid_filter_value(self):
        response = self.client.get(self.url, {'publication_year': 'not_a_number'})
        self.assertEqual(response.status_code, 400)  # Invalid value type

    def test_search_by_title(self):
        response = self.client.get(self.url, {'search': 'Book One'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # Only one book with 'Book One' in the title

    def test_ordering_by_title(self):
        response = self.client.get(self.url, {'ordering': 'title'})
        self.assertEqual(response.status_code, 200)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ['Book One', 'Book Three', 'Book Two'])  # Sorted by title

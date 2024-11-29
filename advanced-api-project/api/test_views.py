from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    """
    Test case for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data and authentication.
        """
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create a few sample books
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2002)

        # Initialize API client and authenticate the user
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books should be returned

    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {"title": "New Book", "author": "New Author", "publication_year": 2023}
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # New book added

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2025}
        response = self.client.put(f'/books/{self.book1.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(f'/books/{self.book2.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # One book deleted

    def test_filter_books(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get('/books/', {'publication_year': 2001})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get('/books/', {'search': 'Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books match "Book"

    def test_order_books(self):
        """
        Test ordering books by title.
        """
        response = self.client.get('/books/', {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book One")

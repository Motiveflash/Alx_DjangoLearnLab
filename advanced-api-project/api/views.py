from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer


class BookGenericAPIView(generics.GenericAPIView):
    """
    Generic API view for managing books with additional functionalities:
    - Permission checks
    - Filtering, searching, and ordering
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    # Define the queryset to fetch all Book objects
    queryset = Book.objects.all()

    # Specify the serializer class
    serializer_class = BookSerializer

    # Add permissions to restrict access to authenticated users only
    permission_classes = [permissions.IsAuthenticated]

    # Filtering and ordering backends
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Specify filterable fields (exact matches)
    filterset_fields = ['publication_year', 'author__name']


    # Enable search on specific fields
    search_fields = ['title', 'author__name']

    # Enable ordering on specific fields
    ordering_fields = ['title', 'publication_year']

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a filtered list of books.

        - Applies filters, search, and ordering.
        - Ensures only authenticated users can access this endpoint.
        """
        books = self.filter_queryset(self.get_queryset())  # Apply filters
        serializer = self.get_serializer(books, many=True)  # Serialize the queryset
        return Response(serializer.data)  # Return the serialized data as a response




class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    - Allows read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Unrestricted access


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a specific book.
    - Allows read-only access for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Unrestricted access


class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

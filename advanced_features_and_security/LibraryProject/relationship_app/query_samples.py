from relationship_app.models import Librarian, Library
from bookshelf.models import Author, Book

# Query all books by a specific author.
def get_book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    print(Book.objects.filter(author=author))


# List all books in a library.
def list_book_in_library(library_name):
    library = Library.objects.get(name=library_name)
    print(library.books.all())

# Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(Librarian.objects.get(library=library))
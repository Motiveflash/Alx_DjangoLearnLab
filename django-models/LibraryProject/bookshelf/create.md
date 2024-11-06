from bookshelf.models import Book

Creating a Book instance

command : Book.objects.create()

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book   

Output: blank space as successful


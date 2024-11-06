from bookshelf.models import Book


Retrieving the book
command: Book.objects.get()

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

output: 1984 George Orwell 1949
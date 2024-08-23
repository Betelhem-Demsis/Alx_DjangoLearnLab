
## python command
from bookshelf.models import Book

new_book = Book.objects.create(title="1984", author="George Orwell", publication_date="1949")

print(new_book)

## expected output 
Book object (1)
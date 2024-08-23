## delete python command
from bookshelf.models import Book
book=Book.objects.get(publication_year="1949")
book.delete()

books = Book.object.all()
print(books)

## expected output 
 QuerySet []

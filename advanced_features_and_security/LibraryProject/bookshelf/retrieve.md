## python command
from bookshelf.models import Book

book=Book.objects.get(publication_year="1949")
 
print(f"Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_year}")

## expected output
Title: 1984, Author: George Orwell, Publication Date: 1949
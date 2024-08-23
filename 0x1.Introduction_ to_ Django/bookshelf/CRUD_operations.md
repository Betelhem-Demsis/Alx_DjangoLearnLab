## create python command
from bookshelf.models import Book

new_book = Book.objects.create(title="1984", author="George Orwell", publication_date="1949")

print(new_book)

## expected output 
Book object (1)


## retrieve python command
from bookshelf.models import Book

book=Book.objects.get(publication_year="1949")
 
print(f"Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_year}")

## expected output
Title: 1984, Author: George Orwell, Publication Date: 1949

## update python command
 from bookshelf.models import Book
 book=Book.objects.get(title="1984") 
 book.title="Nineteen Eighty-Four"
 book.save()
print(f"Updated Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_year}")

## expected output 
Updated Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949

## delete python command
from bookshelf.models import Book
book=Book.objects.get(publication_year="1949")
book.delete()

books = Book.object.all()
print(books)

## expected output 
 QuerySet []

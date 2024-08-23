 
 ## python command
 from bookshelf.models import Book
 book=Book.objects.get(title="1984") 
 book.title="Nineteen Eighty-Four"
 book.save()
print(f"Updated Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_year}")

## expected output 
Updated Title: Nineteen Eighty-Four, Author: George Orwell, Publication Date: 1949

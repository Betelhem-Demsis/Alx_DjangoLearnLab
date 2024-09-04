from django.db import models

# Define the Author model
class Author(models.Model):
    # The name of the author, with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Return the author's name when the object is printed

# Define the Book model
class Book(models.Model):
    # The title of the book, with a maximum length of 200 characters
    title = models.CharField(max_length=200)
    
    # The year the book was published, stored as an integer
    publication_year = models.IntegerField()
    
    # Foreign key linking the book to an author, with cascade deletion
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Return the book's title when the object is printed

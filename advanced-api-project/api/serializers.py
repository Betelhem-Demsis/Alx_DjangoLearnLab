from .models import Author, Book
from rest_framework import serializers
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    # Meta class to define model and fields to be serialized
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

    # Custom validation to check if the publication year is not in the future
    def validate(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError('Publication year should not be in the future')
        return data

class AuthorSerializer(serializers.ModelSerializer):
    # Meta class to define model and fields to be serialized
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields =['id', 'name', 'books']

    def to_representation(self, instance):
     #Custom representation to add the count of books for each author.
        representation = super().to_representation(instance)
        representation['book_count'] = instance.books.count()
        return representation
    
    
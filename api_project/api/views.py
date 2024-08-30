from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset provides the basic CRUD operations over the Book model.

    It uses the BookSerializer to serialize the data to JSON and it uses the
    IsAuthenticated permission class to ensure that only authenticated users can
    access the viewset.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


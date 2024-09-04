from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .filters import BookFilter

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title']  

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class BookDetailView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
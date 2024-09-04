from django.shortcuts import render
from rest_framework import generics
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .seriealizers import BookSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['publication_year', 'author__name']
    ordering_fields = ['title', 'publication_year']

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
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
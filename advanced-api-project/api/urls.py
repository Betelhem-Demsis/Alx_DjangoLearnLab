from django.urls import path
from . import views

urlpatterns = [
    path('/books/', views.BookListView.as_view(),name='book_list'),
    path('/books/create/', views.BookCreateView.as_view(),name='book_create'),
    path('/books/<int:pk>/', views.BookDetailView.as_view(),name='book_detail'),
    path('books/update', views.BookUpdateView.as_view(),name='book_update'),
    path('books/delete', views.BookDeleteView.as_view(),name='book_delete'),
    
]

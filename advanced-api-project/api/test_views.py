from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Book

class BookTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'New Book', 'author': 'John Doe', 'publication_year': 2024}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        data = {'title': 'Unauthorized Book', 'author': 'Jane Doe', 'publication_year': 2025}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def tearDown(self):
        self.book1.delete()
        self.book2.delete()

   
    def test_get_books(self):
        response = self.client.get(reverse('book-list')) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_create_book(self):
        data = {
            'title': 'New Book', 
            'author': 'New Author', 
            'publication_year': 2021
        }
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3) 
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book(self):
        data = {
            'title': 'Updated Book', 
            'author': 'Updated Author', 
            'publication_year': 2020
        }
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')


    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1) 


    def test_filter_books_by_author(self):
        response = self.client.get(reverse('book-list') + '?author=William')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
 
    def test_search_books_by_title(self):
        response = self.client.get(reverse('book-list') + '?search=Django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

   
    def test_order_books_by_title(self):
        response = self.client.get(reverse('book-list') + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Django for Beginners')  
    def test_permission_denied_for_unauthenticated_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('book-list'), {'title': 'Unauthorized Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

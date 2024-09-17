# accounts/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class FollowTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='user1', password='password123')
        self.user2 = CustomUser.objects.create_user(username='user2', password='password123')
        self.client.force_authenticate(user=self.user1)

    def test_follow_user(self):
        url = reverse('follow-user', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user2 in self.user1.following.all())

    def test_unfollow_user(self):
        self.user1.follow(self.user2)
        url = reverse('unfollow-user', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user2 in self.user1.following.all())
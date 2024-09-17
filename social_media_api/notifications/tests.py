from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Notification
from posts.models import Post

User = get_user_model()

class NotificationSystemTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.post = Post.objects.create(author=self.user2, content='Test post')
        self.notification = Notification.objects.create(
            recipient=self.user2,
            actor=self.user1,
            verb='liked your post',
            target=self.post
        )

    def test_list_notifications(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['notifications']), 1)
        self.assertEqual(response.data['unread_count'], 1)

    def test_mark_notification_as_read(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.patch(f'/notifications/{self.notification.id}/mark-read/')
        self.assertEqual(response.status_code, 200)
        self.notification.refresh_from_db()
        self.assertFalse(self.notification.unread)

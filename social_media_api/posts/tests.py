from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from rest_framework.test import APIClient
from .models import Post, Like
from notifications.models import Notification



User = get_user_model()

class LikeSystemTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.post = Post.objects.create(author=self.user2, content='Test post')

    def test_like_post(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Like.objects.filter(user=self.user1, post=self.post).exists())
        self.assertTrue(Notification.objects.filter(recipient=self.user2, actor=self.user1, verb='liked your post').exists())

    def test_unlike_post(self):
        Like.objects.create(user=self.user1, post=self.post)
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(f'/posts/{self.post.id}/unlike/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Like.objects.filter(user=self.user1, post=self.post).exists())


class PostModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            author=self.user,
            title='Test Post',
            content='This is a test post content.'
        )

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test Post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.content}', 'This is a test post content.')
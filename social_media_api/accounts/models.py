from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio=models.TextField(max_length=500, blank=True)
    profile_picture=models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    followers=models.ManyToManyField('self', blank=True)
    following=models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username


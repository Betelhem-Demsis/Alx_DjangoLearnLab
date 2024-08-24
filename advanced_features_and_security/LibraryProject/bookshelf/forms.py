from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

books = Book.objects.raw('SELECT * FROM bookshelf_book WHERE title = "%s"' % user_input)
books = Book.objects.filter(title=user_input)
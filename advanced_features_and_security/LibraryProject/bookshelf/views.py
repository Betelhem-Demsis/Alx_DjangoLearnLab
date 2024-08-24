from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()


def book_list(request):
    books = Book.objects.raw('SELECT * FROM bookshelf_book WHERE title = "%s"' % user_input)
    books = Book.objects.filter(title=user_input)
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    return render(request, 'edit_template.html', {'instance': instance})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_view(request):
    return render(request, 'create_template.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_view(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
   

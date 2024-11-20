from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            books = Book.objects.filter(title__icontains=query) | Book.objects.filter(
                author__first_name__icontains=query) | Book.objects.filter(author__last_name__icontains=query)
        else:
            books = Book.objects.all()

        return render(request, 'home.html', {'books': books, 'query': query})


class BookView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book.html', {'book': book})


class AuthorView(View):
    def get(self, request, author_id):
        # Получаем автора по ID
        author = Author.objects.get(id=author_id)

        # Получаем все книги, написанные этим автором
        books = Book.objects.filter(author=author)

        # Отправляем данные в шаблон
        return render(request, 'author.html', {'author': author, 'books': books})
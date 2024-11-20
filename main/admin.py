from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author')
    search_fields = ('title', 'author__name')
    date_hierarchy = 'publication_date'


class BookInline(admin.StackedInline):
    model = Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    search_fields = ('name',)
    inlines = [BookInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

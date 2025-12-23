from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date']
    list_filter = ['full_name', 'birth_date']
    search_fields = ['full_name', 'birth_date']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_author', 'published_date']
    list_filter = ['title', 'published_date']
    search_fields = ['title', 'author__full_name']

    def get_author(self, obj):
        return ", ".join([author.full_name for author in obj.authors.all()])

    get_author.short_description = "Авторы"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['get_book_title', 'full_name', 'username']
    list_filter = ['full_name', 'username']
    search_fields = ['book__title', 'full_name', 'username']

    def get_book_title(self, obj):
        return ", ".join([book_t.title for book_t in obj.book.all()])

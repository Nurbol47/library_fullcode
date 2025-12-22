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

from django.contrib import admin
from .models import Book, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity_page', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'created_at')
    search_fields = ('book__title',)
    list_filter = ('rating', 'created_at')

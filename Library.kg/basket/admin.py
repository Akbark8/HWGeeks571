from django.contrib import admin
from .models import Customer, BasketItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'quantity', 'added_at')
    search_fields = ('customer__name', 'book__title')
    list_filter = ('added_at',)

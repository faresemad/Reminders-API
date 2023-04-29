from django.contrib import admin
from .models import Reminder, Category
# Register your models here.

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'priority', 'category')
    list_filter = ('priority', 'category')
    search_fields = ('title', 'notes')
    ordering = ('-date', 'time')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ('color',)
    search_fields = ('name',)
    ordering = ('name',)
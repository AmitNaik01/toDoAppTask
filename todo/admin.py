from django.contrib import admin
from .models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "due_date", "timestamp")
    list_filter = ("status", "due_date")

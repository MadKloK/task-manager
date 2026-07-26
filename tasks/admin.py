from django.contrib import admin
from tasks.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'priority', 'status', 'due_date', 'created_at']
    empty_value_display = '-empty-'
    date_hierarchy = 'created_at'
    search_fields = ['priority', 'status', 'user']
    ordering = ['-created_at']
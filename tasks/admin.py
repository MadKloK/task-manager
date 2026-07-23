from django.contrib import admin
from tasks.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'completed', 'created_at']
    empty_value_display = '-empty-'
    date_hierarchy = 'created_at'
    search_fields = ['completed', 'user']
    ordering = ['-created_at']
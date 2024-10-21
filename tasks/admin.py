
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'creation_date')  # Added 'description' field
    list_filter = ('status',)  # Add a filter for status (completed/not completed)
    search_fields = ('title', 'description')  # Add search bar for title and description

# Register the Task model with the custom admin class
admin.site.register(Task, TaskAdmin)

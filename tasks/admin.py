from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    search_fields = ('title', 'description',)

# Register your models here.
admin.site.register(Task, TaskAdmin)
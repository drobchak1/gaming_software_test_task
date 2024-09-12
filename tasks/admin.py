from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    ordering = ('-id',)


admin.site.register(Task, TaskAdmin)

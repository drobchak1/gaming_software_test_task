from django.db import models
from django.utils import timezone


class Task(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    STATUSES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETED, 'Completed'),
    ]

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    PRIORITIES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUSES, default=NEW)
    priority = models.CharField(max_length=20, choices=PRIORITIES, default=LOW)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task with id: {self.id} and title: {self.title}"

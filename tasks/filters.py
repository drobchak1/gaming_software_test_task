from django_filters import rest_framework as filters
from .models import Task


class TaskFilter(filters.FilterSet):
    created_at = filters.DateFilter(field_name='created_at', lookup_expr='date')

    class Meta:
        model = Task
        fields = ['status', 'priority', 'created_at']
from rest_framework import viewsets, mixins
from django_filters import rest_framework as filters

from .filters import TaskFilter
from .paginations import TaskPagination
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer
from .websockets import notify_task_change, notify_task_deleted


class TaskViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter
    pagination_class = TaskPagination

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        notify_task_change("created", task)

    def perform_update(self, serializer):
        task = serializer.save()
        notify_task_change("updated", task)

    def perform_destroy(self, instance):
        task_id = str(instance.id)
        title = str(instance.title)
        instance.delete()
        notify_task_deleted({'id': task_id, 'title': title})

    def list(self, request, *args, **kwargs):
        """
        List all tasks.
        To list all tasks, make a GET request to /api/tasks/

        To filter tasks by status, priority and date of creation, you can use the following query parameters:
            - status: Filter tasks by status (e.g., status=completed)
            - priority: Filter tasks by priority (e.g., priority=medium)
            - created_at: Filter tasks by date of creation (e.g., created_at=2024-09-12)

        To paginate the results, you can use the following query parameters:
            - page: The page number to display (e.g., page=2)
            - page_size: The number of tasks to display per page (e.g., page_size=10)
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create a new task and notify all connected clients.

        To create a new task, make a POST request to /api/tasks/ with the following payload:

            {
                "title": "Task title",
                "description": "Task description",
                "priority": "high",
                "status": "in_progress"
            }
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update a task and notify all connected clients.
        To update a task, make a PUT request to /api/tasks/<task_id>/ with the following payload:

            {
                "title": "Updated task title",
                "description": "Updated task description",
                "priority": "medium",
                "status": "completed"
            }
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a task and notify all connected clients.
        To delete a task, make a DELETE request to /api/tasks/<task_id>/
        """
        return super().destroy(request, *args, **kwargs)

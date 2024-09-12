from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Task


class TaskViewSetTests(APITestCase):
    def setUp(self):
        # Create some tasks to work with
        self.task1 = Task.objects.create(title="Task 1", description="First task", priority=Task.HIGH,
                                         status=Task.IN_PROGRESS)
        self.task2 = Task.objects.create(title="Task 2", description="Second task", priority=Task.MEDIUM,
                                         status=Task.COMPLETED)
        self.task3 = Task.objects.create(title="Task 3", description="Third task", priority=Task.MEDIUM,
                                         status=Task.COMPLETED)
        self.list_url = '/api/tasks/'  # Direct URL for task listing
        self.detail_url = lambda pk: f'/api/tasks/{pk}/'

    def test_list_tasks(self):
        """Test listing task"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)  # Pagination response contains 'results' key
        self.assertEqual(len(response.data['results']), 3)

    def test_list_tasks_with_filters(self):
        """Test listing tasks with filters"""
        response = self.client.get(f'{self.list_url}?status={Task.COMPLETED}&priority={Task.MEDIUM}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)  # Pagination response contains 'results' key
        self.assertEqual(len(response.data['results']), 2)

    def test_create_task(self):
        """Test creating a new task"""
        data = {'title': 'New Task', 'description': 'A new task'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 4)  # Check that a new task is created

    def test_retrieve_task(self):
        """Test retrieving a task by ID"""
        response = self.client.get(self.detail_url(self.task1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)

    def test_update_task(self):
        """Test updating a task (partial and full update)"""
        data = {'title': 'Updated Task', 'description': 'Updated task'}
        response = self.client.put(self.detail_url(self.task1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')

    def test_delete_task(self):
        """Test deleting a task"""
        response = self.client.delete(self.detail_url(self.task1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 2)  # One task deleted

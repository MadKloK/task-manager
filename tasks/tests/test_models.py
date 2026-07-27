from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            title="This test title",
            description="Lets see if it works"
        )

        self.assertEqual(task.title, "This test title")
        self.assertEqual(task.description, "Lets see if it works")
        self.assertEqual(task.user, self.user)

    def test_default_task_status(self):
        task = Task.objects.create(
            user=self.user,
            title="Default Status Test"
        )

        self.assertEqual(task.status, "todo")

    def test_default_task_priority(self):
        task = Task.objects.create(
            user=self.user,
            title="Default Priority Test"
        )

        self.assertEqual(task.priority, "medium")

    def test_task_string_representation(self):
        task = Task.objects.create(
            user=self.user,
            title="My Task"
        )

        self.assertEqual(
            str(task),
            f"{task.id}. My Task"
        )
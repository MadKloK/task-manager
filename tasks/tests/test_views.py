from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from tasks.models import Task


class TaskViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="john",
            password="password123"
        )

        self.task = Task.objects.create(
            user=self.user,
            title="Existing Task",
            description="Test description"
        )


    def test_task_list_requires_login(self):

        response = self.client.get(
            reverse("tasks:task-list")
        )

        self.assertEqual(response.status_code, 302)


    def test_logged_user_can_see_tasks(self):

        self.client.login(
            username="john",
            password="password123"
        )

        response = self.client.get(
            reverse("tasks:task-list")
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            "Existing Task"
        )


    def test_user_can_create_task(self):

        self.client.login(
            username="john",
            password="password123"
        )

        response = self.client.post(
            reverse("tasks:task-create"),
            {
                "title": "New Task",
                "description": "Created by test",
                "priority": "medium",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Task.objects.filter(
                title="New Task"
            ).exists()
        )


    def test_user_can_update_own_task(self):

        self.client.login(
            username="john",
            password="password123"
        )

        response = self.client.post(
            reverse(
                "tasks:task-update",
                args=[self.task.id]
            ),
            {
                "title": "Updated Task",
                "description": "Updated description",
                "status": "done",
                "priority": "high"
            }
        )

        self.assertEqual(response.status_code, 302)

        self.task.refresh_from_db()

        self.assertEqual(
            self.task.title,
            "Updated Task"
        )


    def test_user_can_delete_own_task(self):

        self.client.login(
            username="john",
            password="password123"
        )

        response = self.client.post(
            reverse(
                "tasks:task-delete",
                args=[self.task.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Task.objects.filter(
                id=self.task.id
            ).exists()
        )
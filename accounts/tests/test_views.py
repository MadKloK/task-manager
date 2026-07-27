from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class RegisterViewTest(TestCase):

    def test_user_can_register(self):

        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newuser",
                "password1": "StrongPassword123",
                "password2": "StrongPassword123",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            User.objects.filter(
                username="newuser"
            ).exists()
        )


    def test_registration_password_mismatch(self):

        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newuser",
                "password1": "StrongPassword123",
                "password2": "DifferentPassword123",
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertFalse(
            User.objects.filter(
                username="newuser"
            ).exists()
        )



class LoginViewTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="john",
            password="password123"
        )


    def test_user_can_login(self):

        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "john",
                "password": "password123"
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            response.wsgi_request.user.is_authenticated
        )


    def test_wrong_password_cannot_login(self):

        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "john",
                "password": "wrongpassword"
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertFalse(
            response.wsgi_request.user.is_authenticated
        )



class LogoutViewTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="john",
            password="password123"
        )


    def test_user_can_logout(self):

        self.client.login(
            username="john",
            password="password123"
        )

        self.assertIn(
            "_auth_user_id",
            self.client.session
        )

        response = self.client.post(
            reverse("accounts:logout")
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertNotIn(
            "_auth_user_id",
            self.client.session
        )
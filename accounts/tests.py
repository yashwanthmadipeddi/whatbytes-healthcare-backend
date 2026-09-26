from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AuthenticationTests(APITestCase):

    def test_register_user(self):
        response = self.client.post(
            "/api/auth/register/",
            {
                "name": "Test User",
                "email": "test@example.com",
                "password": "TestPass123!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.filter(email="test@example.com").exists()
        )

    def test_login_returns_jwt_tokens(self):
        User.objects.create_user(
            email="test@example.com",
            name="Test User",
            password="TestPass123!",
        )

        response = self.client.post(
            "/api/auth/login/",
            {
                "email": "test@example.com",
                "password": "TestPass123!",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

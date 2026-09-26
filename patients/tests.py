from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class PatientTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            email="user1@example.com",
            name="User One",
            password="TestPass123!",
        )

        self.user2 = User.objects.create_user(
            email="user2@example.com",
            name="User Two",
            password="TestPass123!",
        )

    def test_unauthenticated_patient_list_is_rejected(self):
        response = self.client.get("/api/patients/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_user_cannot_access_another_users_patient(self):
        self.client.force_authenticate(user=self.user1)

        create_response = self.client.post(
            "/api/patients/",
            {
                "name": "Private Patient",
                "age": 30,
                "gender": "M",
                "phone": "9876543210",
                "address": "Hyderabad",
            },
            format="json",
        )

        self.assertEqual(
            create_response.status_code,
            status.HTTP_201_CREATED,
        )

        patient_id = create_response.data["id"]

        self.client.force_authenticate(user=self.user2)

        response = self.client.get(
            f"/api/patients/{patient_id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class DoctorTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="doctoruser@example.com",
            name="Doctor User",
            password="TestPass123!",
        )

        self.client.force_authenticate(user=self.user)

    def test_create_doctor(self):
        response = self.client.post(
            "/api/doctors/",
            {
                "name": "Dr. Test",
                "specialization": "Cardiologist",
                "phone": "9988776655",
                "email": "doctor@example.com",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["name"],
            "Dr. Test",
        )

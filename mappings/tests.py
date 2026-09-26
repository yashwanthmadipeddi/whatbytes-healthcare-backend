from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from doctors.models import Doctor
from mappings.models import PatientDoctorMapping
from patients.models import Patient

User = get_user_model()


class MappingTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            email="mapping1@example.com",
            name="Mapping User One",
            password="TestPass123!",
        )

        self.user2 = User.objects.create_user(
            email="mapping2@example.com",
            name="Mapping User Two",
            password="TestPass123!",
        )

        self.patient = Patient.objects.create(
            name="Test Patient",
            age=40,
            gender="M",
            phone="9876543210",
            address="Hyderabad",
            created_by=self.user1,
        )

        self.doctor = Doctor.objects.create(
            name="Dr. Mapping",
            specialization="Neurologist",
            phone="9988776655",
            email="mapping.doctor@example.com",
        )

    def test_create_mapping(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.post(
            "/api/mappings/",
            {
                "patient": self.patient.id,
                "doctor": self.doctor.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_duplicate_mapping_is_rejected(self):
        PatientDoctorMapping.objects.create(
            patient=self.patient,
            doctor=self.doctor,
        )

        self.client.force_authenticate(user=self.user1)

        response = self.client.post(
            "/api/mappings/",
            {
                "patient": self.patient.id,
                "doctor": self.doctor.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_user_cannot_map_another_users_patient(self):
        self.client.force_authenticate(user=self.user2)

        response = self.client.post(
            "/api/mappings/",
            {
                "patient": self.patient.id,
                "doctor": self.doctor.id,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

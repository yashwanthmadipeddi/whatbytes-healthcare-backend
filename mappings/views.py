from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.select_related(
            "patient",
            "doctor",
        ).filter(
            patient__created_by=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save()


class MappingPatientListDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        mappings = PatientDoctorMapping.objects.select_related(
            "patient",
            "doctor",
        ).filter(
            patient_id=pk,
            patient__created_by=request.user,
        ).order_by("-created_at")

        serializer = PatientDoctorMappingSerializer(
            mappings,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)

    def delete(self, request, pk):
        mapping = get_object_or_404(
            PatientDoctorMapping.objects.select_related("patient").filter(
                patient__created_by=request.user
            ),
            pk=pk,
        )

        mapping.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

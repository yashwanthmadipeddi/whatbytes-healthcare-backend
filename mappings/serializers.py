from rest_framework import serializers

from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True,
    )

    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True,
    )

    doctor_specialization = serializers.CharField(
        source="doctor.specialization",
        read_only=True,
    )

    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "doctor_specialization",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "patient_name",
            "doctor_name",
            "doctor_specialization",
            "created_at",
        ]

        # Disable DRF's automatic UniqueTogetherValidator
        # so our custom validation message is used.
        validators = []

    def validate(self, attrs):
        patient = attrs["patient"]
        doctor = attrs["doctor"]

        request = self.context.get("request")

        if request and patient.created_by_id != request.user.id:
            raise serializers.ValidationError(
                {
                    "patient": "You can only use patients you created."
                }
            )

        if PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor,
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return attrs

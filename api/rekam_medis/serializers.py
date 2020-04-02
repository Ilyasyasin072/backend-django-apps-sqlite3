from rest_framework import serializers
from .models import MedicalRecord


class MedicalRecordSerialize(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = [
            'id',
            'id_users',
            'date',
            'clock',
            'id_patient',
            'id_doctor',
            'diagnosis',
            'information',
        ]

        class Meta:
            db_table = "medical_record"

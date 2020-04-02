from rest_framework import serializers
from .models import DetailMedicalRecord


class DetailRecordSerialize(serializers.ModelSerializer):
    class Meta:
        model = DetailMedicalRecord
        fields = ['id'
                  'id_medical_record',
                  ]

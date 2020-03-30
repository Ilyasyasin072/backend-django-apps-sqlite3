from rest_framework import serializers
from .models import DetailSchedule


class DetailScheduleSerialize(serializers.ModelSerializer):
    class Meta:
        model = DetailSchedule
        fields = ['id', 'id_patient', 'date']

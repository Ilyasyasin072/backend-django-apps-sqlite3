from rest_framework import serializers
from .models import ScheduleDoctor


class ScheduleDoctorSerialize(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDoctor
        fields = ['id',
                  'id_doctor',
                  'detail_schedule']

from rest_framework import serializers
from .models import ScheduleDoctor


class ScheduleDoctorSerialize(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDoctor
        fields = ['id',
                  'id_doctor',
                  'detail_schedule']

    def __init__(self, *args, **kwargs):
        super(ScheduleDoctorSerialize, self).__init__(*args, **kwargs)
        self.fields['id_doctor'].empty_label = "Select"

from rest_framework import serializers
from .models import RoomPatient


class RoomPatientSerialize(serializers.ModelSerializer):
    class Meta:
        model = RoomPatient
        fields = ['id', 'name_room', 'sum_patient']

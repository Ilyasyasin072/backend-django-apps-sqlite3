from rest_framework import serializers
from .models import Doctor


class DoctorSerialize(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name_doctor', 'specialist', 'age', 'gender', 'address', 'city', 'phone', 'date']

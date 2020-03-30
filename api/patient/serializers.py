from rest_framework import serializers
from .models import Patient


class PatientSerialize(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name_patient', 'address', 'age', 'gender', 'profession', 'name_kk', 'username', 'password']

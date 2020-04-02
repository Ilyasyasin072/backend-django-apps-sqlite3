from django.shortcuts import render
from .serializers import MedicalRecordSerialize
from .models import MedicalRecord
from rest_framework import viewsets
from rest_framework.response import Response


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerialize

    def list(self, request, *args, **kwargs):
        medical_record = MedicalRecord.objects.all()
        serialize = MedicalRecordSerialize(medical_record, many=True)
        return Response(serialize.data)

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerialize
from .models import Patient
from rest_framework.response import Response


# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerialize

    def list(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serialize = PatientSerialize(patients, many=True)
        return Response(serialize.data)
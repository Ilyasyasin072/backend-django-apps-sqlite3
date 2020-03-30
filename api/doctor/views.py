from django.shortcuts import render
from .serializers import DoctorSerialize
from .models import Doctor
from rest_framework import viewsets
from rest_framework.response import Response


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerialize

    def list(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        serialize = DoctorSerialize(doctors, many=True)
        return Response(serialize.data)

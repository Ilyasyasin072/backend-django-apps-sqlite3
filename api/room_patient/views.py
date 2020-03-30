from django.shortcuts import render
from .models import RoomPatient
from .serializers import RoomPatientSerialize
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


class RoomPatientViewSet(viewsets.ModelViewSet):
    queryset = RoomPatient.objects.all()
    serializer_class = RoomPatientSerialize

    def list(self, request, *args, **kwargs):
        room_patient = RoomPatient.objects.all()
        serialize = RoomPatientSerialize(room_patient, many=True)
        return Response(serialize.data)

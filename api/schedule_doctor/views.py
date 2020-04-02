from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ScheduleDoctorSerialize
from .models import ScheduleDoctor


class ScheduleDoctorViewSet(viewsets.ModelViewSet):
    queryset = ScheduleDoctor.objects.all()
    serializer_class = ScheduleDoctorSerialize

    def list(self, request, *args, **kwargs):
        schedule_detail = ScheduleDoctor.objects.all()
        serialize = ScheduleDoctorSerialize(schedule_detail, many=True)
        return Response(serialize.data)


from django.shortcuts import render
from .serializers import DetailScheduleSerialize
from .models import DetailSchedule
from rest_framework.response import Response
from rest_framework import viewsets


class DetailScheduleViewSet(viewsets.ModelViewSet):
    queryset = DetailSchedule.objects.all()
    serializer_class = DetailScheduleSerialize

    def list(self, request, *args, **kwargs):
        detail_schedule = DetailSchedule.objects.all()
        serialize = DetailScheduleSerialize(detail_schedule, many=True)
        return Response(serialize.data)

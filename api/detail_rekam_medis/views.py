from django.shortcuts import render
from .serializers import DetailRecordSerialize
from .models import DetailMedicalRecord
from rest_framework import viewsets
from rest_framework.response import Response


class DetailRecordViewSet(viewsets.ModelViewSet):
    queryset = DetailMedicalRecord.objects.all()
    serializer_class = DetailRecordSerialize

    def list(self, request, *args, **kwargs):
        detail_records = DetailMedicalRecord.objects.all()
        serialize = DetailRecordSerialize(detail_records, many=True)
        return Response(serialize.data)

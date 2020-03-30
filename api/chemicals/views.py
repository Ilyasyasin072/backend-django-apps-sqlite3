from django.shortcuts import render
from .serializers import ChemicalSerialize
from .models import Chemicals
from rest_framework import viewsets
from rest_framework.response import Response


class ChemicalViewSet(viewsets.ModelViewSet):
    queryset = Chemicals.objects.all()
    serializer_class = ChemicalSerialize

    def list(self, request, *args, **kwargs):
        chemical = Chemicals.objects.all()
        serialize = ChemicalSerialize(chemical, many=True)
        return Response(serialize.data)
from rest_framework import serializers
from .models import Chemicals


class ChemicalSerialize(serializers.ModelSerializer):
    class Meta:
        model = Chemicals
        fields = [
            'id',
            'desc_chemical',
            'class_of_drugs',
            'dose',
            'dose_one',
            'purchase_price',
            'selling_price',
            'remaining_medicine',
        ]

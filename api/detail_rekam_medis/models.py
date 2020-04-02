from django.db import models
from rekam_medis.models import MedicalRecord


class DetailMedicalRecord(models.Model):
    id_medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE
    )

    class Meta:
        db_table = "medical_records"

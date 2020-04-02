from django.db import models
from patient.models import Patient
from doctor.models import Doctor


class MedicalRecord(models.Model):
    id_users = models.IntegerField()
    date = models.DateTimeField()
    clock = models.DateTimeField()
    id_patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE
    )
    id_doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE
    )
    diagnosis = models.CharField(max_length=255)
    information = models.CharField(max_length=200)

    class Meta:
        db_table = "medical_record"

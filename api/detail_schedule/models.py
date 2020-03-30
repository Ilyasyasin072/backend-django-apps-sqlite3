from django.db import models
from patient.models import Patient


# Create your models here.

class DetailSchedule(models.Model):
    id_patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        db_table = "detail_schedules"

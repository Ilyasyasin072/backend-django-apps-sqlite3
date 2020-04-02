from django.db import models
from doctor.models import Doctor


class ScheduleDoctor(models.Model):
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    detail_schedule = models.CharField(max_length=100)

    class Meta:
        db_table = "schedule_doctor"


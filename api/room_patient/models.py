from django.db import models


# Create your models here.

class RoomPatient(models.Model):
    name_room = models.CharField(max_length=100)
    sum_patient = models.IntegerField()

    class Meta:
        db_table = "room_patient"

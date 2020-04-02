from django.db import models


class Doctor(models.Model):
    name_doctor = models.CharField(max_length=50)
    specialist = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.IntegerField()
    date = models.DateField()

    class Meta:
        db_table = "doctor"

    def __str__(self):
        return self.name_doctor

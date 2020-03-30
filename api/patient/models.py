from django.db import models


# Create your models here.

class Patient(models.Model):
    name_patient = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    profession = models.CharField(max_length=100)
    name_kk = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)

    class Meta:
        db_table = "patient"

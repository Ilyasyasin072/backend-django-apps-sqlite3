from django.db import models


class Admin(models.Model):
    user_id = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    position = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.IntegerField()
    status = models.CharField(max_length=30)
    education = models.CharField(max_length=50)

    class Meta:
        db_table = "admin"

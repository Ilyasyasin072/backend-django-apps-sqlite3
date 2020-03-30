from django.db import models


# Create your models here.

class Chemicals(models.Model):
    desc_chemical = models.CharField(max_length=100)
    class_of_drugs = models.CharField(max_length=100)
    dose = models.IntegerField()
    dose_one = models.IntegerField()
    purchase_price = models.IntegerField()
    selling_price = models.IntegerField
    remaining_medicine = models.IntegerField()

    class Meta:
        db_table = "chemicals"


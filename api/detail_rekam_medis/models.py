from django.db import models

class DetailMedicalRecord(models.Model):
    id_medical_record = models.ForeignKey(

    )
    class Meta:
        db_table = "medical_records"

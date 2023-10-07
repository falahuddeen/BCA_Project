from django.db import models

# Create your models here.
class EmergencyNumberTable(models.Model):
    em_id = models.AutoField(primary_key=True)
    em_number = models.CharField(max_length=20)
    po_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emergency_number_table'

from django.db import models

# Create your models here.
class PoliceStationTable(models.Model):
    po_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact_number =  models.CharField(max_length=20)
    e_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'police_station_table'

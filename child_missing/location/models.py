from django.db import models

# Create your models here.
class LocationTable(models.Model):
    lo_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'location_table'


class RfidChildLocation(models.Model):
    rf_id = models.AutoField(db_column='RF_ID', primary_key=True)  # Field name made lowercase.
    missing_child_id = models.IntegerField()
    passed_date = models.DateField(db_column='Passed_Date')  # Field name made lowercase.
    passed_time = models.TimeField(db_column='Passed_Time')  # Field name made lowercase.
    passed_location = models.CharField(db_column='Passed_Location', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rfid_child_location'


class MissingCaseTable(models.Model):
    mi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    image = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    verification = models.CharField(db_column='Verification', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'missing_case_table'


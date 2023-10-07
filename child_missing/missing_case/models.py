from django.db import models

# Create your models here.
class MissingCaseTable(models.Model):
    mi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=20)
    image = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    Verification = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'missing_case_table'

from django.db import models

# Create your models here.
class MissingPersionTable(models.Model):
    mis_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    date = models.DateField()
    image = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'missing_persion_table'

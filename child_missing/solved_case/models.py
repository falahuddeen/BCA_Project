from django.db import models

# Create your models here.
class SolvedCaseTable(models.Model):
    s_id = models.AutoField(primary_key=True)
    mi_id = models.IntegerField()
    case = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'solved_case_table'


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

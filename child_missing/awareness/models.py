from django.db import models

# Create your models here.
class AwarenessTable(models.Model):
    aw_id = models.AutoField(primary_key=True)
    awareness = models.CharField(max_length=50)
    date = models.DateField()
    po_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'awareness_table'

from django.db import models
from user.models import UserTable
# Create your models here.
class ComplaintsTable(models.Model):
    c_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=35)
    date = models.DateField()
    time = models.TimeField()
    # u_id = models.IntegerField()
    u=models.ForeignKey(UserTable,to_field='u_id',on_delete=models.CASCADE)
    replay = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'complaints_table'

from django.db import models

# Create your models here.
class UserTable(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=20)
    e_mail = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    adhaar_number =  models.CharField(max_length=50)
    verification = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_table'



from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=30)
    eage=models.IntegerField()
    eaddress=models.CharField(max_length=30)


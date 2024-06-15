from django.db import models

# Create your models here.

class employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    edob=models.DateField()
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=20)
    edob=models.DateField()
    rollno=models.CharField(max_length=10)

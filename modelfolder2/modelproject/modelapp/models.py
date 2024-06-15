from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=20)
    srollno=models.IntegerField()
    sfees=models.IntegerField()
    dob=models.DateField()

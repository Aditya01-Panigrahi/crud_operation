from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    esalary=models.IntegerField()
    
class student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    srollno=models.IntegerField() 
    sdob=models.DateField(null=True)

class Amazon(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField()       

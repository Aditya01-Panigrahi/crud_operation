from django.contrib import admin
from testapp.models import Employee
from testapp.models import student
from testapp.models import Amazon

class studentAdmin(admin.ModelAdmin):
    list_display=['sno','sname','srollno','sdob']

class AmazonAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','product_price']


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esalary']
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(student,studentAdmin)
admin.site.register(Amazon,AmazonAdmin)

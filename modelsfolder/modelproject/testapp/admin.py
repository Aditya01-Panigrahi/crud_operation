from django.contrib import admin
from testapp.models import employee
from testapp.models import student

# Register your models here.
admin.site.register(employee)
admin.site.register(student)

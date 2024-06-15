from django.shortcuts import render
from .models import Employee

# Create your views here.


def search_empname_startswith(request, search_string):
    employees = Employee.objects.filter(fname__startswith=search_string)
    return render(request, 'empapp/employee_list.html', {'employees': employees})

def search_empname_contains(request, search_string):
    employees = Employee.objects.filter(fname__contains=search_string)
    return render(request, 'empapp/employee_list.html', {'employees': employees})

def search_empage_lte(request, age):
    employees = Employee.objects.filter(age__lte=age)
    return render(request, 'empapp/employee_list.html', {'employees': employees})

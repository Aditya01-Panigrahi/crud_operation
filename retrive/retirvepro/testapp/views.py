from django.shortcuts import render
from testapp.models import Employee

def displaydate(request):
    employees=Employee.objects.all()
    return render (request,'testapp/result.html',{'employees':employees})
# Create your views here.

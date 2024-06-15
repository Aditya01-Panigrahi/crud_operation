from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    date=datetime.datetime.now()
    k={'date':date}
    return render(request,"studentapp/student.html",context=k)

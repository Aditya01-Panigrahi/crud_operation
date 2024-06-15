from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    date=datetime.datetime.now()
    d={'date':date}
    return render(request,'cssapp/result.html',context=d)
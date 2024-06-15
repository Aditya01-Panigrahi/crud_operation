from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    dt=datetime.datetime.now()
    ke={'date':dt}
    return render(request,'dynamicapp/results.html',context=ke)
from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    return render(request,'formapp/home.html')
def login(request):
    return render(request,'formapp/login.html')
def register(request):
    return render(request, 'formapp/register.html')
def datetimes(request):
    dt=datetime.datetime.now()
    ke={'date':dt}
    return render(request, 'formapp/click.html',context=ke)    
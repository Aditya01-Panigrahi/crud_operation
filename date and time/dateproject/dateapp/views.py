#from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.
def displaydatetime(request):
    date=datetime.datetime.now()
    a='<h1> current date and time:'+str(date)+'</h1>'
    return HttpResponse(a)
def message(request):
    return  HttpResponse("hii welcome to odisha")



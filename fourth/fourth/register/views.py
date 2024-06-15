from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.
def datetimes(request):
    a='<h1> the time is:'+str(datetime.datetime.now())
    return HttpResponse(a)

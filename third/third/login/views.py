from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.
def datetimes(request):
    a='<h1> The time is:'+str(datetime.datetime.now())+'</h1>'
    return HttpResponse(a)

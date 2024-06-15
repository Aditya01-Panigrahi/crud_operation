from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.
def displaydatetime(request):
    a='<h1> date and time is:'+str(datetime.datetime.now())+'</h1>'
    return HttpResponse(a)

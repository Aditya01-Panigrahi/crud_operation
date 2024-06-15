from django.shortcuts import render
import datetime
# Create your views here.
def datetimes(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        #return render(request,'application/mor.html')
        msg="good morning"
    elif h<16:
        msg="good afternoon"
    elif h<21:
        msg="good evening"
    else:
        msg="good night"            
    
    response=render(request,'application/c.html',{'m':msg,'date':date})
    return response


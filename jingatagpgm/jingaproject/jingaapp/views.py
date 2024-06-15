from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    dt=datetime.datetime.now()

    if (dt.time().hour<12):
        msg = "GOOD MORINIG"
    elif (dt.time().hour>=12):
        msg="GOOD AFTERNOON"
    elif (dt.time().hour>=5):
        msg="evening"
    else:
        msg="GOOD NIGHT"

    a={'date':dt,"message":msg}
    return render(request,'jingaapp/result.html',context=a)


    
    

from django.shortcuts import render
import datetime

# Create your views here.
def display(request):
    dt=datetime.datetime.now()
   
    d=int(dt.strftime('%H'))
    if d<12 and d>4:
        msg="good morning"
    elif d>=12 and d<16:
        msg="good afternoon"
    elif d>16 and d<20:
        msg="good evening"
    else:
        msg="good night"           
        ke={'date':dt,'m':msg}

    return render(request,'cosmeticapp/result.html',context=ke)

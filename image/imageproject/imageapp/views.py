from django.shortcuts import render
import datetime

# Create your views here.
def imagesdisplay(request):
    dt=datetime.datetime.now()
    k={'date':dt}
    return render(request,"imageapp/result.html",context=k)

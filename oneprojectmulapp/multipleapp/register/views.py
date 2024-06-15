from django.shortcuts import render,HttpResponse

# Create your views here.
def displaymsg(request):
    return HttpResponse("hello everyone welcome to itvedant")

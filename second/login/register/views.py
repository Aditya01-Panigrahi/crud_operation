from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def accesss(request):
    return HttpResponse("welcome to python. hii i am aditya")

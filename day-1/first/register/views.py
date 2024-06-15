
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def access(request):
    return HttpResponse("welcome to python")
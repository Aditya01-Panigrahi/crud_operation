from django.shortcuts import render, HttpResponse

# Create your views here.
def display(request):
    return HttpResponse('welcome to application level url')

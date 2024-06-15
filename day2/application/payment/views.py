from django.shortcuts import render,HttpResponse

# Create your views here.
def accept(request):
    return HttpResponse("The payment is successfully.")

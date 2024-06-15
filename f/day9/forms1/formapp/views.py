from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,'formapp/login.html')
def display1(request):
    return render(request,'formapp/register.html')
def display2(request):
    return render(request,'formapp/submit.html')
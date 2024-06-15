from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request,'Form_app/home.html')

def Loginpage(request):
    return render(request,'Form_app/login.html')

def Register(request):
    return render(request,'Form_app/register.html')

def ClickMe(request):
    return render(request,'Form_app/clickme.html')


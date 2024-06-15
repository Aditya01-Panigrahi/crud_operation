from django.shortcuts import render

# Create your views here.\
def display(request):
    return render(request,'from2app/login.html')
def register(request):
    return render(request,'from2app/register.html')
def home(request):
    return render(request,'from2app/home.html')
def add(request):
    return render(request,'from2app/add.html')

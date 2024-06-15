from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'form_app/home.html')
def login(request):
    return render(request,'form_app/login.html')

from django.shortcuts import render,HttpResponse

# Create your views here.
def dispaly(request):
    return HttpResponse("nice class")

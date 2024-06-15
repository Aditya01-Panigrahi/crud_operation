from django.contrib import admin
from django.urls import path
from NETFLIXAPP import views

app_name='NETFLIXAPP'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name='Home') , 
]
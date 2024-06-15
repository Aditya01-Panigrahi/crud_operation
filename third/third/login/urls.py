from django.contrib import admin
from django.urls import path
from login import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', v1.datetimes),
]
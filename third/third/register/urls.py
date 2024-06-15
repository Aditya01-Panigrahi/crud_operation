from django.contrib import admin
from django.urls import path
from register import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('b/', v2.display),
]
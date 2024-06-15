# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.service_page, name='service_page'),
    # Add more URL patterns as needed
]

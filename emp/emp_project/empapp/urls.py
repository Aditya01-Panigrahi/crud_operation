from django.urls import path
from . import views

urlpatterns = [
    path('empname/startswith/<str:search_string>/', views.search_empname_startswith, name='search_empname_startswith'),
    path('empname/contains/<str:search_string>/', views.search_empname_contains, name='search_empname_contains'),
    path('empage/lte/<int:age>/', views.search_empage_lte, name='search_empage_lte'),
]
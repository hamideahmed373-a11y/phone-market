from .views import *
from django.urls import path

urlpatterns = [
    path('',phones,name='home'),
]
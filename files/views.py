from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *


def phones(request):
    phone=Phone.objects.all()
    return render(request,'phone.html',{'products':phone})





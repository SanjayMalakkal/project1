from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def intro(request):
    return render(request,'user/home.html')

def abt(request):
    return render(request,'user/about.html')

def cont(request):
    return render(request,'user/contact.html')

def new(request):
    return render(request,'user/new.html')
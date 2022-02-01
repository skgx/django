from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse("hello world")
    return render(request,'home.html',{'name':'saurabh'})

def add(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    res=num1+num2

    return render(request,'result.html',{'result':res})
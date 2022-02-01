from datetime import datetime
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.messages import constants as messages
# Create your views here.

def index(request):
    context={
        'variable1':"Saurabh here!",
        'variable2':'How are you'
    }
    messages.success(request,"this is test")
    return render(request,'index.html',context)
    #return httpResponse("this is home page")

def about(request):
    return render(request,'about.html',)
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html',)
    #return HttpResponse("this is services page")

def contact(request):
 if request.method=='POST': 
     name=request.POST.get('name')
     email=request.POST.get('email')
     desc=request.POST.get('desc')
     contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
     contact.save()
     messages.success(request, 'message sent!')
 return render(request,'contact.html',)
    #return HttpResponse("this is contacts page")


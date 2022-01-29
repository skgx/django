from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context={
        'variable1':"Saurabh here!",
        'variable2':'How are you'
    }
    return render(request,'index.html',context)
    #return httpResponse("this is home page")

def about(request):
    return render(request,'about.html',)
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html',)
    #return HttpResponse("this is services page")

def contact(request):
    return render(request,'contact.html',)
    #return HttpResponse("this is contacts page")

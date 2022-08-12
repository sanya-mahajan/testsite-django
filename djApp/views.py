from django.shortcuts import render,HttpResponse,redirect
#rendering for response as templates
from datetime import datetime
from django.contrib.auth.models import User
from userAuth import views #for using the login view

from .models import data

#attributs views.attribute




from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    context ={
        'variable':"value of the var in CONTEXT sent with index.html",
        'variable2':"context is a dictionary!"

    }
    
    

    return render(request,'index.html',context)
    
def about(request):
    names=[]
    
    for val in data.objects.all():
        names.append(val.name)  
    
    context={
        'info': names,
        
    }

    

    return render(request,'abt.html',context)  
def services(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        quote=request.POST.get('quote')
        adjective=request.POST.get('adjective')

        #every entry is a class instance
        entry= data(name=name,quote=quote,adjective=adjective, date=datetime.today())#constructor
        entry.save()
        
        #dj messages framework
        from django.contrib import messages
        messages.success(request, 'submitted!')
        
        
    return render(request,'serv.html')



def your_space(request):
    names=[]

    
        
         
            
            
    context={
        'set' : data.objects.all(),
        'qname' : request.POST.get('inpname')  #ummm
    }
    



    return render(request,'quotes.html',context)    
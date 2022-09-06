
from django.urls import reverse
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
#rendering for response as templates
from datetime import datetime
from django.contrib.auth.models import User
from userAuth import views #for using the login view
from django import forms
from .models import data,mood

#attributs views.attribute




from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):

    if(request.method=="POST"):
        
        myform =mood(request.POST)
        if myform.is_valid():
            feels=myform.cleaned_data['mood_field']
            context ={
                
                'feels': feels

    }
            return render(request,'index.html',context)#dont encode urls directly
    
    
    context={
        'moodform': mood
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
    

    name= request.POST.get('inpname')
    if data.objects.filter(name=name).exists():
        context={
        'set' : data.objects.all(),
        'qname' : request.POST.get('inpname')  
    }
        return render(request,'quotes.html',context)    
    else:
        from django.contrib import messages
        messages.info(request,'please submit your data')
        return HttpResponseRedirect(reverse('servicespage'))
        
    

    
        
         
            
            
    
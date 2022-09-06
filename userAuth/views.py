from django.urls import reverse
from http.client import HTTP_PORT
from urllib import response
from django.shortcuts import render,HttpResponse,redirect


from django.contrib.auth import authenticate,logout,login #in built user model
from django.contrib.auth.models import User
from djApp import views
import djApp
import userAuth
from djApp.models import mood

# Create your views here.


def loginusr(request):
    if(request.method=="POST"):
        usrname=request.POST.get('usrname')
        pswd=request.POST.get('pswd')
        is_usr= authenticate(request, username=usrname, password=pswd)
        #check correct credentials
        if(is_usr!=None):
            login(request,is_usr)
            context={
                'uname': request.POST.get('usrname') ,
                
            }
            
            return render(request,'index.html',context)
        else:
            if(User.objects.filter(username=usrname)):
                context={
                    'error_message': "wrong password"
                }
                return render(request,'login.html',context)





            else:    
                context={
                    'error_message': "user not registered"
                }
                return render(request,'login.html',context)

    return render(request , 'login.html')

def register(request):
    return HttpResponse("reg")    

def logoutusr(request):
    logout(request)
    return render(request,'logout.html')
    

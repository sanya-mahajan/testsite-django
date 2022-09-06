from django.contrib import admin
from django.urls import path
from userAuth import views
import djApp

urlpatterns = [
    path('login',views.loginusr,name="loginpage"),
    path('logout',views.logoutusr,name="logoutpage"),
    path('register',views.register,name="registerpage"),
    

]

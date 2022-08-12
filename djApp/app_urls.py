

from django.urls import path
from djApp import views #app view 


urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('about',views.about,name='aboutpage'),
    path('services',views.services,name='servicespage'),
    path('your_space',views.your_space,name='quotepage')
]

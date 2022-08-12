from django.contrib import admin
from django.urls import path,include

#first arrives at urls of main project file 
#URL DISPATCHING

#i the bawse
admin.site.site_header="sanya admin"
admin.site.site_title="title=testsite"
admin.site.index_title="you go girl!"


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('userAuth.app_urls')),
    path('',include('djApp.app_urls'))

]




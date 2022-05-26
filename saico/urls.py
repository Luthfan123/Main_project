"""saico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('login/',views.login1),
    path('about/',views.about),
    path('log/',views.log),
    path('adminhome/',views.adminhome),
    path('staffhome/',views.staffhome),
    path('addcategory/',views.addcategory),
    path('category1/',views.category1),
    path('removecategory/',views.removecategory), 
    path('deletecategory/<int:id>',views.deletecategory), 
    path('addproduct/',views.addproduct), 
    path('products1/',views.products1),
    path('removeproduct/',views.removeproduct), 
    path('updateproduct/',views.updateproduct), 
   

    path('deleteproduct/<int:id>',views.deleteproduct), 
    path('addstaff/',views.addstaff),
    path('addstaff1/',views.addstaff1),
    path('removestaff/',views.removestaff), 
    path('deletestaff/<int:id>',views.deletestaff), 
    path('adddealer/',views.adddealer),
    path('adddealer1/',views.adddealer1),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

   
    


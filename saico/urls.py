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
    path('dealerhome/',views.dealerhome),
    path('addcategory/',views.addcategory),
    path('category1/',views.category1),
    path('removecategory/',views.removecategory), 
    path('deletecategory/<str:id>',views.deletecategory), 
    path('addproduct/',views.addproduct), 
    path('products1/',views.products1),
    path('removeproduct/',views.removeproduct), 
    path('updateproduct/',views.updateproduct), 
    path('removedealer/',views.removedealer), 
    
    
    path('deletedealer/<str:id>',views.deletedealer), 
    path('deleteproduct/<str:id>',views.deleteproduct), 
    path('addstaff/',views.addstaff),
    path('addstaff1/',views.addstaff1),
    path('removestaff/',views.removestaff), 
    path('deletestaff/<str:id>',views.deletestaff), 
    path('adddealer/',views.adddealer),
    path('adddealer1/',views.adddealer1),
    path('stockupdate/',views.stockupdate),
    path('stockupdate1/<str:id>',views.stockupdate1),
    path('updateproduct/<str:id>',views.updateproduct),
    path('stockupdate2/<str:id>',views.stockupdate2),
    path('viewproducts/',views.viewproducts),
    path('orderproduct/<str:id>',views.orderproduct),
    path('orderproduct1/<str:id>',views.orderproduct1),
    path('finishorder/',views.finishorder),
    path('payments1/',views.payments1),
    path('vieworder/',views.vieworder),
    path('processorder1/<str:id>',views.processorder1),
    path('viewpayment/<str:id>',views.viewpayment),
    path('acceptorder/<str:id>',views.acceptorder),
    path('rejectorder/<str:id>',views.rejectorder),
    path('approveorders/',views.approveorders),
    path('rejectorders/',views.rejectorders),
    path('viewpayment1/<str:id>',views.viewpayment1),
    path('approveorders1/<str:id>',views.approveorders1),
    path('rejectorders1/<str:id>',views.rejectorders1),
    path('search/',views.search),
    path('pendingorders/',views.pendingorders),
    path('pendingorders1/<str:id>',views.pendingorders1),
    path('delivery1/',views.delivery1),
    path('deliverystatus/',views.deliverystatus),
    path('deliverystatus1/<str:id>',views.deliverystatus1),
    path('pendingordersdealer/',views.pendingordersdealer),
    path('pending1/<str:id>',views.pending1),
    path('cancelorder/',views.cancelorder),
    path('cancelorder1/<str:id>',views.cancelorder1),
    path('cancelorder2/<str:id>',views.cancelorder2),
    path('cancelreason1/<str:id>',views.cancelreason1),
    path('viewcancelorder/',views.viewcancelorder),
    path('viewreason/<str:id>',views.viewreason),
    path('viewreason1/<str:id>',views.viewreason1),







]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

   
    


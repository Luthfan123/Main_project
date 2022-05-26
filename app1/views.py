from django.shortcuts import render,redirect,HttpResponse
from app1.models import login,category,products,staff,dealer
from django.core.files.storage import FileSystemStorage
from datetime import date
tday=date.today()
def login1(request):
    return render(request,"login.html")
def index(request):
    return render(request,"index.html")    
def about(request):
    return render(request,"about.html")    
def log(request):
    if request.method == 'POST':
        dataa=login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        
        flag=0
            
        for da in dataa:
            
            if un == da.username and pwd == da.password:
               
    
                
                type=da.category
                request.session['uid']=un
                flag = 1
                if type=="admin":
                    return redirect('/adminhome')   
                elif type=="staff":
                    
                    return redirect('/staffhome')  
                elif type=="customer":
                    
                    return redirect('/customers1')  
                elif type=="shop":
                    
                    return redirect('/shop2') 
                elif type=="deliveryboy":
                    
                    return redirect('/deliveryboy1')      

                
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("Invalid user")        
def adminhome(request):
    return render(request,"adminhome.html")     
def staffhome(request):
    return render(request,"staffhome.html")          
def addcategory(request):
   return render(request,"addcategory.html")                    

def category1(request):
    if request.method == 'POST' :
       cat = category()
       cat.cat_id="na"
       cat.cat_name=request.POST.get('name')
       Photo = request.FILES['photo']
       fs = FileSystemStorage()
       filename = fs.save(Photo.name, Photo) 
       uploaded_file_url = fs.url(filename)
       cat.photo=uploaded_file_url
       cat.save()

       cat.cat_id = "CAT_00" + str(cat.id)
       cat.save()
    return render(request,"addcategory.html")
def removecategory(request):
   items= category.objects.all()
   return render(request,"remove_category.html",{'items1':items})


def deletecategory(request,id):
   items = category.objects.get(id=id)
   items.delete()
   return redirect('/removecategory')    
def addstaff(request):
    print("--------------------------",tday)
    return render(request,"addstaff.html",{"today1":tday})                    

def addstaff1(request):
    if request.method == 'POST' :
       cat = staff()
       cat.staff_id="na"
       cat.name=request.POST.get('name')
       cat.address=request.POST.get('address')
       cat.gender=request.POST.get('gender')
       cat.phone=request.POST.get('phone')
       cat.email=request.POST.get('email')
       cat.doj=request.POST.get('doj')
       cat.qualification=request.POST.get('qualification')
       cat.department=request.POST.get('department')
       cat.post=request.POST.get('post')
       cat.save()

       cat.cat_id = "STAFF_00" + str(cat.id)
       cat.save()
       data=login()
       data.username="STAFF_00" + str(cat.id)
       data.password=request.POST.get('phone')
       data.category="staff"
       data.save()
    return render(request,"addstaff.html")
def adddealer(request):
   return render(request,"adddealer.html")                    

def adddealer1(request):
    if request.method == 'POST' :
       cat = dealer()
       cat.dealer_id="na"
       cat.name=request.POST.get('name')
       cat.address=request.POST.get('address')
       cat.phone=request.POST.get('phone')
       cat.officename=request.POST.get('officename')
       cat.officeaddress=request.POST.get('officeaddress')
       cat.city=request.POST.get('city')
       cat.state=request.POST.get('state')
       cat.email=request.POST.get('email')
       cat.dealershipdate=request.POST.get('dealershipdate')
       cat.save()

       cat.cat_id = "Dealer_00" + str(cat.id)
       cat.save()
    return render(request,"adddealer.html")    
def removestaff(request):
   items= staff.objects.all()
   return render(request,"remove_staff.html",{'items1':items})


def deletestaff(request,id):
   items = staff.objects.get(id=id)
   items.delete()
   return redirect('/removestaff')       
def addproduct(request):
   data=category.objects.all()
   return render(request,"addproduct.html",{'data':data})

def products1(request):
   if request.method == 'POST' :
       pro = products()
       pro.prod_id="na"
       pro.cat_id=request.POST.get('cat_id')
       pro.name=request.POST.get('name')
       pro.description=request.POST.get('description')
       Photo = request.FILES['photo']
       fs = FileSystemStorage()
       filename = fs.save(Photo.name, Photo) 
       uploaded_file_url = fs.url(filename)
       pro.photo=uploaded_file_url
       pro.unitprice=request.POST.get('unitprice')
       pro.unit=request.POST.get('unit')
       
       pro.quantity=request.POST.get('quantity')
       
       pro.expiredate=request.POST.get('expiredate')
       pro.manifacturedate=request.POST.get('manifacturedate')
       pro.save()

       pro.prod_id = "PROD_00" + str(pro.id)
       pro.save()
   return redirect('/addproduct')
def removeproduct(request):
   items= products.objects.all()
   return render(request,"remove_products.html",{'items1':items})

def updateproduct(request):
   items= products.objects.all()
   return render(request,"update_products.html",{'items1':items})

def deleteproduct(request,id):
   items = products.objects.get(id=id)
   items.delete()
   return redirect('/removeproduct')




# Create your views here.

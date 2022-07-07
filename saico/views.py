from django.shortcuts import render,redirect,HttpResponse
from app1.models import login,category,products,staff,tbl_return,dealer,tbl_feedback,tbl_idgen,tbl_complaint,tbl_dealerorderdetails,dealerorder, tbl_payment,tbl_delivery,tbl_cancel
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Sum
import datetime
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
                elif type=="dealer":
                    
                    return redirect('/dealerhome')  
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
def dealerhome(request):
    return render(request,"dealerhome.html")               
def addcategory(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.cid
    id = int(id+1)
    cid = "CATEGORY_00" + str(id)
    request.session["cid"] = id
    request.session["cid1"] = cid
    return render(request,"addcategory.html")                    

def category1(request):
    if request.method == 'POST' :
       cat = category()
        
       cat.cat_id=request.session["cid1"]
       cat.cat_name=request.POST.get('name')
       Photo = request.FILES['photo']
       fs = FileSystemStorage()
       filename = fs.save(Photo.name, Photo) 
       uploaded_file_url = fs.url(filename)
       cat.photo=uploaded_file_url
       cat.save()
       data1=tbl_idgen.objects.get(id=1)
       data1.cid=request.session['cid']
       data1.save()
       return render(request,"addcategory.html",{'data':1})      
    
def removecategory(request):
   items= category.objects.all()
   return render(request,"remove_category.html",{'items1':items})


def deletecategory(request,id):
   items = category.objects.get(cat_id=id)
   items.delete()
   return redirect('/removecategory')    
def addstaff(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.sid
    id = int(id+1)
    sid = "STAFF_00" + str(id)
    request.session["sid"] = id
    request.session["sid1"] = sid
    return render(request,"addstaff.html")                    

def addstaff1(request):
    if request.method == 'POST' :
       cat = staff()
       cat.staff_id=request.session["sid1"]
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

       data1=tbl_idgen.objects.get(id=1)
       data1.sid=request.session['sid']
       data1.save()
       data=login()
       data.username=request.session["sid1"]
       data.password=request.POST.get('phone')
       data.category="staff"
       data.save()
    return render(request,"addstaff.html",{'data':1})
def adddealer(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.did
    id = int(id+1)
    did = "DEALER_00" + str(id)
    request.session["did"] = id
    request.session["did1"] = did
    return render(request,"adddealer.html")                    

def adddealer1(request):
    if request.method == 'POST' :
       cat = dealer()
       cat.dealer_id=request.session["did1"]
       cat.name=request.POST.get('name')
       cat.address=request.POST.get('address')
       cat.phone=request.POST.get('phone')
       cat.officename=request.POST.get('officename')
       cat.officeaddress=request.POST.get('officeaddress')
       cat.city=request.POST.get('city')
       cat.state=request.POST.get('state')
       cat.email=request.POST.get('email')
       cat.dealershipdate=request.POST.get('dealershipdate')
       cat.status="verified"
       cat.save()

       data1=tbl_idgen.objects.get(id=1)
       data1.did=request.session['did']
       
       data1.save()
       data=login()
       data.username=request.session["did1"]
       data.password=request.POST.get('phone')
       data.category="dealer"
       data.save()
    return render(request,"adddealer.html",{'data':1})    
def removestaff(request):
   items= staff.objects.all()
   return render(request,"remove_staff.html",{'items1':items})


def deletestaff(request,id):
   items = staff.objects.get(staff_id=id)
   items.delete()
   items1=login.objects.get(username=id)
   items1.delete()
   return redirect('/removestaff')       
def addproduct(request):
    data=category.objects.all()
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.pid
    id = int(id+1)
    pid = "PRODUCT_00" + str(id)
    request.session["pid"] = id
    request.session["pid1"] = pid
    return render(request,"addproduct.html",{'data':data})

def products1(request):
   if request.method == 'POST' :
       pro = products()
       pro.prod_id=request.session["pid1"]
       pro.cat_id_id=request.POST.get('cat_id')
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
       
       pro.expiredate=request.POST.get('expirydate')
       pro.manifacturedate=request.POST.get('manufacturedate')
       pro.save()

       data1=tbl_idgen.objects.get(id=1)
       data1.pid=request.session['pid']
       data1.save()
       data=category.objects.all()
   return render(request,"addproduct.html",{'data2':1,'data':data})
def removeproduct(request):
   items= products.objects.all()
   return render(request,"remove_products.html",{'items1':items})
def removedealer(request):
   items= dealer.objects.filter(status="verified")
   return render(request,"removedealer.html",{'items1':items})

def verifydealer(request):
   items= dealer.objects.filter(status="notverified")
   return render(request,"verifydealer.html",{'items1':items})

def updateproduct(request):
   items= products.objects.all()
   return render(request,"update_products.html",{'items1':items})

def deleteproduct(request,id):
   items = products.objects.get(prod_id=id)
   items.delete()
   return redirect('/removeproduct')
   
def verifydealer1(request,id):
   items = dealer.objects.get(dealer_id=id)
   items.status="verified"
   items.save()
   data=login()
   data.username=items.dealer_id
   data.password=items.phone
   data.category="dealer"
   data.save()

   return redirect('/verifydealer') 


def deletedealer(request,id):
   items = dealer.objects.get(dealer_id=id)
   items.delete()
   items1=login.objects.get(username=id)
   items1.delete()
   return redirect('/removedealer')   
def stockupdate(request):
   items= products.objects.all()
   return render(request,"stockupdate.html",{'items1':items})   
def stockupdate1(request,id):
   items= products.objects.get(prod_id=id)
   return render(request,"stockupdate1.html",{'items1':items})     
def updateproduct(request,id):
   items= products.objects.get(prod_id=id)
   return render(request,"updateproduct.html",{'items1':items})    
def stockupdate2(request,id):
   items= products.objects.get(prod_id=id)
   items.quantity=request.POST.get('quantity')
   items .expiredate=request.POST.get('expiredate')
   items.manifacturedate=request.POST.get('manifacturedate')
   items.save()
   return redirect('/stockupdate')
def viewproducts(request):
   items= products.objects.all()
   return render(request,"viewproducts.html",{'items1':items})    
def orderproduct(request,id):
    items=products.objects.get(prod_id=id)
    items1=dealer.objects.get(dealer_id=request.session['uid'])
    return render(request,'orderform.html',{'items':items,'items1':items1})    
def orderproduct1(request,id):
    data=tbl_dealerorderdetails()
    if 'oid' not in request.session:
        data4=products.objects.get(prod_id=id)
        u=int(data4.quantity)
        q=int(request.POST.get('quantity'))
        p=int(u-q)
        pid=id
        if p<0:
            return HttpResponse("stock not available.......only available "+str(u))
        else:
            data1 = tbl_idgen.objects.get(id=1)
            id = data1.odid
            id = int(id+1)
            odid = "ORDERDETAILS_00" + str(id)
            request.session["odid"] = id
            request.session["odid1"] = odid
            id = data1.orid
            id = int(id+1)
            orid = "ORDER" + str(id)
            request.session["orid"] = id
            request.session["orid1"] = orid
            data2=products.objects.get(prod_id=pid)
            data.prod_id_id=pid
            data.quantity=request.POST.get('quantity')
            q=int(request.POST.get('quantity'))
            amt=int(request.POST.get('price'))
            net=int(q*amt)
            data.amount=net
            data.status="pending"
            data.orderdet_id=request.session["odid1"]
            data.order_id=request.session["orid1"]
            data.save()
            data2 = tbl_idgen.objects.get(id=1)
            data2.odid=request.session['odid']
            data2.save()
            request.session['oid']=request.session["orid1"]
            data10=products.objects.all()
            return render(request,'viewproducts.html',{'items1':data10}) 
           
    else:
        data4=products.objects.get(prod_id=id)
        u=int(data4.quantity)
        q=int(request.POST.get('quantity'))
        p=int(u-q)
        pid=id
        if p<0:
            return HttpResponse("stock not available.......only available "+str(u))
        else:
            data2=products.objects.get(prod_id=pid)
            data.prod_id_id=pid
            data.quantity=request.POST.get('quantity')
            q=int(request.POST.get('quantity'))
            amt=int(request.POST.get('price'))
            net=int(q*amt)
            data.amount=net
            data.status="pending"
            data1 = tbl_idgen.objects.get(id=1)
            id = data1.odid
            id = int(id+1)
            odid = "ORDERDETAILS_00" + str(id)
            request.session["odid"] = id
            request.session["odid1"] = odid
            
            data.orderdet_id=request.session["odid1"]
            data.order_id=request.session["oid"]
            data.save()
            data2 = tbl_idgen.objects.get(id=1)
            data2.odid=request.session['odid']
            data2.save()
            data10=products.objects.all()
            return render(request,'viewproducts.html',{'items1':data10})     
def finishorder(request):
            if 'oid' not in request.session:
                return HttpResponse("please choose products..............")
            else:

    
                oo=request.session['oid']
                amount =tbl_dealerorderdetails.objects.filter(order_id=oo).aggregate(sum=Sum('amount'))['sum']
                data = dealerorder()
                data.order_id = request.session['oid']
                data.dealer_id_id =request.session['uid']
                now = datetime.datetime.now()
                time = now.strftime('%y-%m-%d')
                data.order_date = time
                data.amount=amount
                data.status="pending"
                data.paymentstatus="pending"
                data.save()
                data1 = tbl_idgen.objects.get(id=1)
                data1.orid=request.session['orid']
                data1.save()
                
                return render(request,"payments.html",{'a':amount,'id':request.session['oid'],'d':request.session['uid']})   



def payments1(request):
    data=tbl_payment()
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.p1id
    id = int(id+1)
    p1id = "PAYMENT_00" + str(id)
    request.session["p1id"] = id
    data.payment_id=p1id
    data.order_id_id=request.POST.get('orderid')
    data.dealer_id_id=request.POST.get('dealerid')
    data.bank_name=request.POST.get('bank')
    data.amount=request.POST.get('amount')
    data.ifsc=request.POST.get('ifsc')
    data.accnumber=request.POST.get('acc_number')
    data.payment_mode=request.POST.get('mode')
    data.status="pending"
    data.save()
    data1.p1id=request.session["p1id"]
    data1.save()
    del request.session['oid']
    data10=products.objects.all()
    return render(request,'viewproducts.html',{'items1':data10,'s1':1})     
def vieworder(request):
 items= dealerorder.objects.filter(status="pending")
 return render(request,"process_order.html",{'items1':items})




def processorder1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="pending")
   return render(request,"viewdetails.html",{'items1':items,'z':id})
def viewpayment(request,id):
   items=tbl_payment.objects.filter(order_id=id)
   return render(request,"viewpayment.html",{'items1':items})

def acceptorder(request,id):




    oo=id

    tdt=tbl_dealerorderdetails.objects.filter(order_id=id) 
    for ct in tdt:
        
        data4=products.objects.get(prod_id=ct.prod_id_id)
        u=int(data4.quantity)
        q=int(ct.quantity)
        p=int(u-q)
        if p<0:
            return HttpResponse("stock not available.......only available "+str(u))
        else:
            ct.status="Order Accepted"
            ct.save()
            data5=products.objects.get(prod_id=ct.prod_id_id)
            u=int(data5.quantity)
            q=int(ct.quantity)
            
            p=int(u-q)
            data5.quantity=p
            data5.save()

            count = tbl_dealerorderdetails.objects.filter(order_id=ct.order_id).filter(status="pending").count()
            if count==0:
                data3=dealerorder.objects.get(order_id=ct.order_id)
                data3.status = "completed"
                data3.save()
            #data1 = tbl_dealerorderdetails.objects.filter(order_id=ct.order_id).filter(status="pending")
                data1 = tbl_idgen.objects.get(id=1)
                id = data1.dlid
                id = int(id+1)
                dlid = "DELIVERY_00" + str(id)
                request.session["dlid"] = id
                request.session["dlid1"] = dlid
                return render(request,"delivery.html",{'o1':oo,'o2':data3.dealer_id_id})
      





    
def rejectorder(request,id):
    data = tbl_dealerorderdetails.objects.get(orderdet_id=id)
    data.status = "Order Rejected"
    data.save()
    count = tbl_dealerorderdetails.objects.filter(order_id=data.order_id).filter(status="pending").count()
    if count==0:
        data1=dealerorder.objects.get(order_id=data.order_id)
        data1.status = "completed"
        data1.save()
    data1 = tbl_dealerorderdetails.objects.filter(order_id=data.order_id).filter(status="pending")

    return render(request,"viewdetails.html",{'items1':data1})
def approveorders(request):
 items= dealerorder.objects.filter(status="completed").order_by('-order_date')
 return render(request,"approveorders.html",{'items1':items})


def pendingorders(request):
 items= dealerorder.objects.filter(status="pending")
 return render(request,"pendingorders.html",{'items1':items})

def approveorders1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="Order Accepted")
   return render(request,"approveorders1.html",{'items1':items})
def viewpayment(request,id):
   items=tbl_payment.objects.filter(order_id=id)
   return render(request,"viewpayment.html",{'items1':items})
def viewpayment1(request,id):
   items=tbl_payment.objects.filter(order_id=id)
   return render(request,"viewpayment1.html",{'items1':items})
def rejectorders(request):
 items= dealerorder.objects.filter(status="completed")
 return render(request,"rejectorders.html",{'items1':items})

def pendingorders1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="pending")
   return render(request,"pendingorders1.html",{'items1':items})


def approveorders1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="Order Accepted")
   return render(request,"approveorders1.html",{'items1':items})   
def rejectorders1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="Order Rejected")
   return render(request,"rejectorders1.html",{'items1':items})  
def search(request):   
    data = request.POST.get('search')
    # data2 = products.objects.all()
    # data5=[];  
    # data6=[];  
    # for x in data2: 
    #     p=x.name.lower()
    #     data5.append(p)
    # for y in data5:
    #     if data in y:
    #         data6.append(y)   
    # for s in data6:
    if data:
        result=products.objects.filter(name__icontains=data)
        return render(request,'viewproducts.html',{'items1':result})   
    return render(request,"vieworder.html")     
def delivery1(request):
    data=tbl_delivery()
    data.delivery_id=request.session['dlid1']
    data.order_id_id=request.POST.get('orderid')
    data.dealer_id_id=request.POST.get('dealerid')
    data.date=request.POST.get('date')
    data.time=request.POST.get('time')
    data.status="pending"
    data.save()
    data1 = tbl_idgen.objects.get(id=1)
    data1.dlid=request.session['dlid']
    data1.save()
    
    return render(request,"staffhome.html")        
def deliverystatus(request):
 items= dealerorder.objects.filter(status="completed").filter(dealer_id_id=request.session['uid'])
 return render(request,"deliverystatus.html",{'items1':items})   
def deliverystatus1(request,id):
 items=tbl_delivery.objects.get(order_id_id=id)
 return render(request,"deliverystatus1.html",{'pr':items})    
def pendingordersdealer(request):
 items= dealerorder.objects.filter(status="pending").filter(dealer_id_id=request.session['uid'])
 return render(request,"pendingordersdealer.html",{'items1':items})    
def pending1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="pending")
   return render(request,"pending1.html",{'items1':items,'z':id})
def cancelorder(request):
 items= dealerorder.objects.filter(status="pending").filter(dealer_id_id=request.session['uid'])
 return render(request,"cancelorder.html",{'items1':items})   
def cancelorder1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="pending")
   return render(request,"cancelorder1.html",{'items1':items,'z':id}) 
def cancelorder2(request,id):
   items=tbl_dealerorderdetails.objects.get(orderdet_id=id)
   data1 = tbl_idgen.objects.get(id=1)
   id = data1.cnid
   id = int(id+1)
   cnid = "CANCEL_00" + str(id)
   request.session["cnid"] = id
   request.session["cnid1"] = cnid               
   return render(request,"cancelreason.html",{'items1':items}) 
def cancelreason1(request,id):
    items=tbl_dealerorderdetails.objects.get(orderdet_id=id)
    items.status="cancelled"
    items.save()
    data=tbl_cancel()
    data.cancel_id=request.session['cnid1']
    data.orderdet_id_id=id
    now = datetime.datetime.now()
    time = now.strftime('%y-%m-%d')
    data.cancel_date=time
    data.status="pending"
    data.cancel_reason=request.POST.get('reason')
    data.save()
    data1 = tbl_idgen.objects.get(id=1)
    data1.cnid=request.session['cnid']
    data1.save()
    items1=tbl_dealerorderdetails.objects.filter(order_id=items.order_id).filter(status="pending")
    return render(request,"cancelorder1.html",{'items1':items1,'z':id}) 
def viewcancelorder(request):
 items=tbl_dealerorderdetails.objects.filter(status="cancelled")
 return render(request,"viewcancelorder.html",{'items1':items,'z':id})
def viewreason(request,id):
 items1=tbl_cancel.objects.get(orderdet_id_id=id)
 return render(request,"viewreason.html",{'pr':items1})
def viewreason1(request,id):
 items1=tbl_cancel.objects.get(cancel_id=id)
 items1.status="cancel accepted"
 items1.save()
 items=tbl_dealerorderdetails.objects.get(orderdet_id=items1.orderdet_id_id)
 items.status="cancel order"
 items.save()
 count = tbl_dealerorderdetails.objects.filter(order_id=items.order_id).filter(status="pending").count()
 if count==0:
        data3=dealerorder.objects.get(order_id=items.order_id)
        data3.status="cancelled"
        data3.save()
        return render(request,"staffhome.html")
 else:
        items=tbl_dealerorderdetails.objects.filter(order_id=items.order_id).filter(status="pending")
        return render(request,"cancelorder1.html",{'items1':items,'z':id}) 

def addcomplaint(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.comid
    id = int(id+1)
    cid = "COMPLAINT_00" + str(id)
    request.session["comid"] = id
    request.session["comid1"] = cid
    return render(request,"addcomplaint.html")                    

def addcomplaint1(request):
    if request.method == 'POST' :
       cat = tbl_complaint()
        
       cat.complaint_id=request.session["comid1"]
       cat.complaint=request.POST.get('complaint')
       cat.dealer_id_id=request.session['uid']
       now = datetime.datetime.now()
       time = now.strftime('%d-%m-%Y')
       cat.date = time
       cat.status="pending"
       cat.save()
       data1=tbl_idgen.objects.get(id=1)
       data1.comid=request.session['comid']
       data1.save()
       return render(request,"addcomplaint.html",{'data':1})      
def viewcomplaint(request):
    data=tbl_complaint.objects.filter(status="pending")
    return render(request,"viewcomplaint.html",{'items1':data})      
def approvecomplaint(request,id):
    data=tbl_complaint.objects.get(complaint_id=id)
    data.status="approved"
    data.save()
    return redirect('/viewcomplaint') 
def complaintstatus(request):
    data=tbl_complaint.objects.filter(dealer_id_id=request.session['uid'])
    return render(request,"complaintstatus.html",{'items1':data})      
def addfeedback(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.fid
    id = int(id+1)
    cid = "FEEDBACK_00" + str(id)
    request.session["fid"] = id
    request.session["fid1"] = cid
    return render(request,"addfeedback.html")                    

def addfeedback1(request):
    if request.method == 'POST' :
       cat = tbl_feedback()
        
       cat.feedback_id=request.session["fid1"]
       cat.feedback=request.POST.get('feedback')
       cat.dealer_id_id=request.session['uid']
       now = datetime.datetime.now()
       time = now.strftime('%d-%m-%Y')
       cat.date = time
       
       cat.save()
       data1=tbl_idgen.objects.get(id=1)
       data1.fid=request.session['fid']
       data1.save()
       return render(request,"addfeedback.html",{'data':1})   
def viewproductspublic(request):
   items= products.objects.all()
   return render(request,"viewproductspublic.html",{'items1':items})              
def searchpublic(request):   
    data = request.POST.get('search')
    # data2 = products.objects.all()
    # data5=[];  
    # data6=[];  
    # for x in data2: 
    #     p=x.name.lower()
    #     data5.append(p)
    # for y in data5:
    #     if data in y:
    #         data6.append(y)   
    # for s in data6:
    if data:
        result=products.objects.filter(name__icontains=data)
        return render(request,'viewproductspublic.html',{'items1':result})   
    else:
        items= products.objects.all()
        return render(request,"viewproductspublic.html",{'items1':items}) 
def dealerreg(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.did
    id = int(id+1)
    did = "DEALER_00" + str(id)
    request.session["did"] = id
    request.session["did1"] = did
    return render(request,"dealerreg.html")                    

def dealerreg1(request):
    if request.method == 'POST' :
       cat = dealer()
       cat.dealer_id=request.session["did1"]
       cat.name=request.POST.get('name')
       cat.address=request.POST.get('address')
       cat.phone=request.POST.get('phone')
       cat.officename=request.POST.get('officename')
       cat.officeaddress=request.POST.get('officeaddress')
       cat.city=request.POST.get('city')
       cat.state=request.POST.get('state')
       cat.email=request.POST.get('email')
       cat.dealershipdate=request.POST.get('dealershipdate')
       cat.status="notverified"
       cat.save()


       data1=tbl_idgen.objects.get(id=1)
       data1.did=request.session['did']
       
       data1.save()
       
    return render(request,"dealerreg.html",{'data':1})            

            

def returnorder(request):
 items= dealerorder.objects.filter(status="completed").filter(dealer_id_id=request.session['uid'])
 return render(request,"returnorder.html",{'items1':items})   
def returnorder1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id).filter(status="Order Accepted")
   return render(request,"returnorder1.html",{'items1':items,'z':id}) 
def returnorder2(request,id):
   items=tbl_dealerorderdetails.objects.get(orderdet_id=id)
   data1 = tbl_idgen.objects.get(id=1)
   id = data1.rid
   id = int(id+1)
   cnid = "RETURN_00" + str(id)
   request.session["rid"] = id
   request.session["rid1"] = cnid               
   return render(request,"returnreason.html",{'items1':items}) 
def returnreason1(request,id):
    items=tbl_dealerorderdetails.objects.get(orderdet_id=id)
    items.status="returned"
    items.save()
    data=tbl_return()
    data.return_id=request.session['rid1']
    data.orderdet_id_id=id
    now = datetime.datetime.now()
    time = now.strftime('%y-%m-%d')
    data.date=time
    data.status="pending"
    data.dealer_id_id=request.session['uid']
    data.return_reason=request.POST.get('reason')
    data.save()
    data1 = tbl_idgen.objects.get(id=1)
    data1.rid=request.session['rid']
    data1.save()
    items1=tbl_dealerorderdetails.objects.filter(order_id=items.order_id).filter(status="Order Accepted")
    return render(request,"returnorder1.html",{'items1':items1,'z':id}) 
def viewreturnorder(request):
 items=tbl_dealerorderdetails.objects.filter(status="returned")
 return render(request,"viewreturnorder.html",{'items1':items,'z':id})
def returnviewreason(request,id):
 items1=tbl_return.objects.get(orderdet_id_id=id)
 return render(request,"returnviewreason.html",{'pr':items1})
def returnviewreason1(request,id):
 items1=tbl_return.objects.get(return_id=id)
 items1.status="return accepted"
 items1.save()
 items=tbl_dealerorderdetails.objects.get(orderdet_id=items1.orderdet_id_id)
 items.status="return order accepted"
 items.save()
 count = tbl_dealerorderdetails.objects.filter(order_id=items.order_id).filter(status="Order Accepted").count()
 if count==0:
        data3=dealerorder.objects.get(order_id=items.order_id)
        data3.status="returned all"
        data3.save()
        return render(request,"staffhome.html")
 else:
        items=tbl_dealerorderdetails.objects.filter(order_id=items.order_id).filter(status="Order Accepted")
        return render(request,"returnorder1.html",{'items1':items,'z':id}) 


def returnstatus(request):
   items=tbl_return.objects.filter(dealer_id_id=request.session['uid'])
   return render(request,"returnstatus.html",{'items1':items})


def returnstatusadmin(request):
   items=tbl_return.objects.all()
   return render(request,"returnstatusadmin.html",{'items1':items})


def productreport(request):
   items= products.objects.all()
   return render(request,"productreport.html",{'items1':items})  


def salesreport(request):
 items= dealerorder.objects.all()
 return render(request,"salesreport.html",{'items1':items})




def salesreport1(request,id):
   items=tbl_dealerorderdetails.objects.filter(order_id=id)
   return render(request,"salesreport1.html",{'items1':items,'z':id})


def editprofile(request):
    uid=request.session['uid']
    data=dealer.objects.get(dealer_id=uid)
    return render(request,"editprofile.html",{'data':data})

def editprofile1(request,id):
    if request.method == 'POST' :
       cat =dealer.objects.get(dealer_id=id)
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

    return render(request,"dealerhome.html")    


def editprofilestaff(request):
    uid=request.session['uid']
    data=staff.objects.get(staff_id=uid)
    return render(request,"editprofilestaff.html",{'data':data})

def editprofilestaff1(request,id):
    if request.method=='POST':
       cat =staff.objects.get(dealer_id=id)
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

    return render(request,"staffhome.html")    
  
# Create your views here.

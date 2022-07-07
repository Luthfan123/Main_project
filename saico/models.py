from django.db import models
class login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
  

class Meta:
      db_table = "login"
class category(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=30)
    cat_name = models.CharField(max_length=60)
    photo = models.CharField(max_length=80)

class Meta:
      db_table = "category"

class products(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=30)
    cat_id =models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=80)
    photo = models.CharField(max_length=40)
    unitprice = models.CharField(max_length=60)
    unit = models.CharField(max_length=60)
    quantity = models.CharField(max_length=60)
    remark= models.CharField(max_length=40)
    expiredate= models.CharField(max_length=40)
    manifacturedate= models.CharField(max_length=40)
    

class Meta:
      db_table = "products"
class staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    gender = models.CharField(max_length=80)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    doj = models.CharField(max_length=60)
    qualification = models.CharField(max_length=60)
    department = models.CharField(max_length=60)
    post = models.CharField(max_length=60)
    remark= models.CharField(max_length=40)
    

class Meta:
      db_table = "staff"      
class dealer(models.Model):
    dealer_id =models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    officename = models.CharField(max_length=60)
    officeaddress = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    dealershipdate = models.CharField(max_length=60)
    remark= models.CharField(max_length=40)
    status= models.CharField(max_length=40)
    

class Meta:
      db_table = "dealer"    
  
class dealerorder(models.Model):
    order_id=models.CharField(primary_key=True, max_length=30)
    dealer_id=models.ForeignKey(dealer, on_delete=models.CASCADE)
    order_date=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    paymentstatus=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="dealerorder"  
class tbl_dealerorderdetails(models.Model):
    orderdet_id=models.CharField(primary_key=True, max_length=30)
    order_id=models.CharField(max_length=30)
    prod_id=models.ForeignKey(products, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    amount=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_dealerordersetails"            
class tbl_payment(models.Model):
    payment_id=models.CharField(primary_key=True, max_length=30)
    order_id=models.ForeignKey(dealerorder, on_delete=models.CASCADE)
    dealer_id=models.ForeignKey(dealer, on_delete=models.CASCADE)
    bank_name=models.CharField(max_length=30)
    ifsc=models.CharField(max_length=30)
    accnumber=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    payment_mode=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_payment"                   
class tbl_idgen(models.Model):
    cid = models.IntegerField()
    comid = models.IntegerField()
    pid = models.IntegerField()
    did = models.IntegerField()
    sid = models.IntegerField() 
    odid= models.IntegerField()    
    orid= models.IntegerField() 
    p1id= models.IntegerField()   
    dlid= models.IntegerField()   
    cnid= models.IntegerField()   
    fid= models.IntegerField()  
    rid= models.IntegerField()  
class tbl_delivery(models.Model):
    delivery_id=models.CharField(primary_key=True, max_length=30)
    order_id=models.ForeignKey(dealerorder, on_delete=models.CASCADE)
    dealer_id=models.ForeignKey(dealer, on_delete=models.CASCADE)
    status=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_delivery"        
class tbl_cancel(models.Model):
    cancel_id=models.CharField(primary_key=True, max_length=30)
    orderdet_id=models.ForeignKey(tbl_dealerorderdetails, on_delete=models.CASCADE)
    cancel_reason=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    cancel_date=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_cancel"       
class tbl_complaint(models.Model):
    complaint_id=models.CharField(primary_key=True, max_length=30)
    dealer_id=models.ForeignKey(dealer, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_complaint"        
class tbl_feedback(models.Model):
    feedback_id=models.CharField(primary_key=True, max_length=30)
    dealer_id=models.ForeignKey(dealer, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_feedback"      
class tbl_return(models.Model):
    return_id=models.CharField(primary_key=True, max_length=30)
    orderdet_id=models.ForeignKey(tbl_dealerorderdetails, on_delete=models.CASCADE)
    dealer_id=models.ForeignKey(dealer, on_delete=models.CASCADE)
    return_reason=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_return"                         

                   

# Create your models here.

from django.db import models
class login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
  

class Meta:
      db_table = "login"
class category(models.Model):
    cat_id = models.CharField(max_length=40)
    cat_name = models.CharField(max_length=60)
    photo = models.CharField(max_length=80)

class Meta:
      db_table = "category"

class products(models.Model):
    prod_id = models.CharField(max_length=40)
    cat_id = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=80)
    photo = models.CharField(max_length=40)
    unitprice = models.CharField(max_length=60)
    unit = models.CharField(max_length=60)
    quantity = models.CharField(max_length=60)
    stockquantity = models.CharField(max_length=60)
    remark= models.CharField(max_length=40)
    expiredate= models.CharField(max_length=40)
    manifacturedate= models.CharField(max_length=40)
    

class Meta:
      db_table = "products"
class staff(models.Model):
    staff_id = models.CharField(max_length=40)
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
    dealer_id = models.CharField(max_length=40)
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
    

class Meta:
      db_table = "dealer"            

# Create your models here.

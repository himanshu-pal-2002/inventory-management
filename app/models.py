from email.headerregistry import Address
from itertools import product
from pickle import TRUE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# vendor
class Vendor(models.Model):
    full_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="vendor/")
    address=models.TextField()
    mobile=models.CharField(max_length=15)
    status=models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural='1. Vendors'
    
    def __str__(self):
        return self.full_name
# Unit
class Unit(models.Model):
    tittle=models.CharField(max_length=50)
    short_name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural='2. Units'
    
    def __str__(self):
        return self.tittle

# Product
class Product(models.Model):
    tittle=models.CharField(max_length=50)
    detail=models.TextField()
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="product/")
    
    class Meta:
        verbose_name_plural='3. product'

    def __str__(self):
        return self.tittle 
    
# Purchase
class Purchase(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    qty=models.FloatField()
    price=models.FloatField()
    total_amt=models.FloatField(editable=False,default=0)
    pur_date=models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        verbose_name_plural='4. Purchase'
    def save(self,*args,**kwargs):
        self.total_amt=self.qty*self.price
        super(Purchase, self).save(*args,**kwargs)
        # Inventory Effect
        inventory=Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
           totalBal=inventory.total_bal_qty+self.qty
        else:
           totalBal=self.qty
        
        Inventory.objects.create(
           product=self.product,
           purchase=self,
           Sales=None,
           pur_qty=self.qty,
           sale_qty=None,
           total_bal_qty=totalBal
    )
        
        
        
        
        
# Sales
class Sales(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.FloatField()
    price=models.FloatField()
    total_amt=models.FloatField(editable=False)
    sale_date=models.DateTimeField(auto_now_add=True) 
    
    customer_name=models.CharField(max_length=50,blank=True)
    customer_mobile=models.CharField(max_length=50)
    customer_address=models.TextField()
    
    class Meta:
        verbose_name_plural='5. Sales'
    
    def save(self,*args,**kwargs):
        self.total_amt=self.qty*self.price
        super(Sales, self).save(*args,**kwargs)
        # Inventory Effect
        inventory=Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
           totalBal=inventory.total_bal_qty-self.qty
        
        Inventory.objects.create(
           product=self.product,
           purchase=None,
           Sales=self,
           pur_qty=None,
           sale_qty=self.qty,
           total_bal_qty=totalBal
    )    
        
#Inventory
class Inventory(models.Model):
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE,default=0,null=True)
   Sales=models.ForeignKey(Sales,on_delete=models.CASCADE,default=0,null=True)
   pur_qty=models.FloatField(default=0,null=True)
   sale_qty=models.FloatField(default=0,null=True)
   total_bal_qty=models.FloatField()
    
   class Meta:
       verbose_name_plural='6. Inventory'
       
   def product_unit(self):
        return self.product.unit.tittle
          
   def pur_date(self):
       if self.purchase:
           return self.purchase.pur_date
       
   def sale_date(self):
       if self.Sales:
           return self.Sales.sale_date

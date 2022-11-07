from django.contrib import admin
from . import models

admin.site.register(models.Vendor)
admin.site.register(models.Unit)

class ProductAdmin(admin.ModelAdmin):
    list_display=['tittle','unit']
admin.site.register(models.Product,ProductAdmin)

class Purchaseadmin(admin.ModelAdmin):
    list_display=['id','product','qty','price','total_amt','vendor','pur_date']  
admin.site.register(models.Purchase,Purchaseadmin)

class SalesAdmin(admin.ModelAdmin):
    list_display=['id','product','qty','price','total_amt','sale_date']  
admin.site.register(models.Sales,SalesAdmin)

class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product_title','product_unit_title']
    list_display=['product','pur_qty','sale_qty','total_bal_qty','product_unit','pur_date','sale_date']  
admin.site.register(models.Inventory,InventoryAdmin)
# Register your models here.

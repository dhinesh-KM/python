#from django.db import models
from djongo import models
from bson.decimal128 import Decimal128
from decimal import Decimal


# Create your models here.
class product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    #quantity = models.DecimalField(max_digits=10,decimal_places=3,default=0.00)
    quantity = models.IntegerField()
    discount = models.IntegerField(default=0)
    
    def __str__(self): 
        return f"{self.product_id} {self.name} {self.price} {self.quantity} {self.discount}"
    
    '''def update(self,quantity):
        #s = self.quantity.to_decimal()
        
        print(type(s))
        t = s - quantity
        print("-",t,Decimal128(t))
        self.quantity = Decimal128(t)
        self.save()
        #self.quantity -= quantity
        #self.save()'''
    
    class Meta:
        db_table = 'products'
         


    

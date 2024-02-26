from djongo import models
from invent.models import product
from accounts.models import CustomUser



class Order(models.Model):
    o_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prod = models.ForeignKey(product, on_delete=models.CASCADE)
    o_product = models.CharField(max_length=50)
    #o_quantity = models.DecimalField(max_digits=10, decimal_places=3)
    #t_price = 
    o_quantity = models.IntegerField()
    o_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Orders"
        
class bill(models.Model):
    t_price = models.IntegerField()
    
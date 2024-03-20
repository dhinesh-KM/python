#from django.db import models
from djongo import models
from customer.models import CustomUser
#auth imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class product(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.FloatField()
    discount = models.IntegerField(default=0)
    #user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    
    #quantity = models.DecimalField(max_digits=10,decimal_places=3,default=0.00)
    
    def __str__(self): 
        return f"{self.name} have a quantity of {self.quantity} with a price of {self.price} with {self.discount} percent discount"
    

    
    class Meta:
        db_table = 'products'
         

'''@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    '''


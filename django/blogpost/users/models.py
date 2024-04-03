from djongo import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    _id = models.ObjectIdField()
    
    class Meta:
        db_table = 'Users'
    

        
    def __str__(self):
        return f"{self.username}"
    
    def fields(self):
        return f"{self.username} have {self.email},{self.first_name},{self.last_name},{self.password}"
    
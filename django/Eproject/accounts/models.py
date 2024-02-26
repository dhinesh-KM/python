from djongo import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    choices = [
        ("M","Male"),
        ("F","Female"),
        ("O","Others")
    ]
    gender = models.CharField(max_length=1,choices=choices)
    
    class Meta:
        db_table  ="Users"

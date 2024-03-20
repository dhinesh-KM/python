from djongo import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
#auth imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class CustomUser(AbstractUser):
    country = models.CharField(max_length = 100)
    
    class Meta:
        db_table = 'Users'
        
    def __str__(self):
        return f"{self.username} with a {self.password} live in {self.country}"
    
    def get_country_display(self):
        return self.country.name
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
#from django.db import models
from djongo import models
from users.models import CustomUser
# Create your models here.

class Blog(models.Model):
    category = models.CharField(max_length = 30)


class Post(models.Model):
    blog = models.ManyToManyField(Blog)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class comment(models.Model):
    user = models.ForeignKey('Post' , on_delete = models.CASCADE)
    comment = models.TextField()
    comment_at = models.DateTimeField(auto_now_add = True)
    
    
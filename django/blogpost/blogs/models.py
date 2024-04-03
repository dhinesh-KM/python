from django.db import models
from djongo import models
from users.models import CustomUser
# Create your models here.


class Post(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = 'Post'
    
    def __str__(self) :
        return f"{self.title}"
    
class Comment(models.Model):
    _id = models.ObjectIdField()
    post = models.ForeignKey(Post , on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = 'Comment'
    
    def __str__(self) :
        return f"{self.post.title}"
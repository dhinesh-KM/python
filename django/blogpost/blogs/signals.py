from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Comment,Post

@receiver([post_save,post_delete], sender=Comment)
def update_comments_cache(sender, instance, **kwargs):
    cache.delete('All_comments')
    

    
@receiver([post_save,post_delete], sender=Post)
def update_comments_cache(sender, instance, **kwargs):
    cache.delete('All_posts')
    
@receiver([post_save,post_delete], sender=Comment)
def update_comments_cache(sender, instance, **kwargs):
    cache.delete_pattern('pk*')
       


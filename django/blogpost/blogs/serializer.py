from .models import Post,Comment
from rest_framework import serializers
from users.models import CustomUser
from users.serializer import RegisterSerializer
from bson import ObjectId
from rest_framework.response import Response
from rest_framework import status
from bson.errors import InvalidId
from rest_framework.exceptions import APIException
from blogs import exceptions



        
class PostSerializer(serializers.ModelSerializer):
    
    comment_set = serializers.HyperlinkedRelatedField( many = True,read_only=True,view_name='gup-comment')
    author = serializers.ReadOnlyField(source = 'author.username')
    id = serializers.CharField(source='_id', read_only = True)
    class Meta:
        model = Post
        fields = ["id","title", "content", "author", "publication_date","comment_set"]
        
    
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    post_id = serializers.CharField()
    post = serializers.ReadOnlyField(source = 'post.title')
    class Meta:
        model = Comment
        fields = ['_id','user', 'post_id', 'post','comment', 'comment_at']
        read_only_fields = ['_id']


    def create(self, validated_data):
        post = validated_data.pop('post_id') 
        try:
            post = Post.objects.get(pk=ObjectId(post))
            #print(True)
            
        except Post.DoesNotExist:
            raise exceptions.Not_Found(name="comment")
        
        except InvalidId:
            raise exceptions.Invalid_Id(pk = self.kwargs['pk'])
        
        comment = Comment.objects.create(post=post, **validated_data)
        return comment
    
    def update(self, instance, validated_data):

        post_id = validated_data.pop('post_id', instance.post_id)
    
        if post_id:
            try:
                post = Post.objects.get(pk=ObjectId(post_id))
                
            except Post.DoesNotExist:
                raise exceptions.Not_Found(name="post")
            
            except InvalidId:
                raise exceptions.Invalid_Id(pk = self.kwargs['pk'])
            
            instance.post = post
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        
        return instance


 
        

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,permissions
from .serializer import PostSerializer,CommentSerializer
from .models import Post,Comment
from bson import ObjectId
from django.core.exceptions import ObjectDoesNotExist
from bson.errors import InvalidId
from .permissions import IsAuthorOrReadOnly,IsUserOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from blogpost import custom_exceptions
from django.core.cache import cache
import redis

# Create your views here.

redis_instance = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

class create_post(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
    
    def create(self, request, *args, **kwargs):
        #print("Current user:", request.user)
        response =  super().create(request, *args, **kwargs)
        response = {'error': False,'msg': 'Post created successfully','data': response.data}
        return Response(response, status=status.HTTP_201_CREATED)
    
class get_post(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    #@method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        cache_key = 'All_posts'
        if cache_key in cache:
            print('redis')
            queryset = cache.get(cache_key)
            return Response(queryset)
        else:
            response = super().list(request, *args, **kwargs)
            print("no cache")
            cache.set(cache_key,response.data,timeout=60*5)
            return Response({'error': False, 'data': response.data}, status= status.HTTP_200_OK)
    
class gup_post(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    
    def get_object(self):
        
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=ObjectId(self.kwargs['pk']))
            self.check_object_permissions(self.request, obj)
            return obj
        
        except ObjectDoesNotExist:
            raise custom_exceptions.Not_Found(name = "post")
        
        except InvalidId:
            raise custom_exceptions.Invalid_Id(pk = self.kwargs['pk'])

        
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status=status.HTTP_200_OK)
    
        
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'error': False, 'msg': 'post  deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class create_comment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
    
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        response = {'error': False,'msg': 'comment created successfully','data': response.data}
        return Response(response, status=status.HTTP_201_CREATED)
        
    
class get_all_comment(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    #@method_decorator(cache_page(30))
    def list(self, request, *args, **kwargs):
        cache_key = 'All_comments'
        if cache_key in cache:
            print('redis')
            queryset = cache.get(cache_key)
            return Response(queryset)
        else:
            response = super().list(request, *args, **kwargs)
            print("no cache")
            cache.set(cache_key,response.data,timeout=60*5)
            return Response({'error': False, 'data': response.data}, status= status.HTTP_200_OK)
    
class get_comment(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    
    #@method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        post_id = self.request.query_params.get('pk') #self.kwargs['pk']
        cache_key = 'pk' + post_id

        if cache_key in cache:
            print("redis")
            queryset = cache.get(cache_key)
            return Response(queryset)
        else:
            print('db')
            print(post_id)
            try: 
                c = self.queryset.get( pk = ObjectId(post_id))
                comments = c.comment_set.all()
                if not comments:
                    return Response({'error':True,'detail': 'there is no comment exist for this comment'}, status= status.HTTP_200_OK)
                
                #page = self.paginate_queryset(queryset)
                #print('page',page)
                #if page is not None:
                #    serializer = self.get_serializer(page, many=True)
                #   return self.get_paginated_response(serializer.data)'''
                serializer = self.get_serializer(comments, many=True)
                cache.set(cache_key,serializer.data,timeout=30)
                return Response({'error': False, 'data': serializer.data}, status= status.HTTP_200_OK)
            
            except ObjectDoesNotExist:
                print(True)
                raise custom_exceptions.Not_Found(name="post")
            
            except InvalidId:
                raise custom_exceptions.Invalid_Id(pk = post_id)
            
    
    
class gup_comment(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOrReadOnly]
    
    def get_object(self):
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=ObjectId(self.kwargs['pk']))
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise custom_exceptions.Not_Found(name="comment")
        
        except InvalidId:
            raise custom_exceptions.Invalid_Id(pk = self.kwargs['pk'])
        
        
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status=status.HTTP_200_OK)
    
        
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'error': False, 'msg': 'comment  deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
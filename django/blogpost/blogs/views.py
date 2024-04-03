from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,permissions
from .serializer import PostSerializer,CommentSerializer
from .models import Post,Comment
from bson import ObjectId
from django.core.exceptions import ObjectDoesNotExist
from bson.errors import InvalidId
from .permissions import IsAuthorOrReadOnly,IsUserOrReadOnly
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import APIException
from django.shortcuts import get_object_or_404
# Create your views here.

class create_post(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
    
    def create(self, request, *args, **kwargs):
        print("Current user:", request.user)
        response =  super().create(request, *args, **kwargs)
        response = {'error': False,'msg': 'Post created successfully','data': response.data}
        return Response(response, status=status.HTTP_201_CREATED)
    
class get_post(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {'error': False, 'data': response.data}
        return Response(response, status= status.HTTP_200_OK)
    
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
            raise APIException({'error': True, 'msg': 'Post  not found ' })
        
        except InvalidId:
            raise APIException({'error': True, 'msg': f'Invalid post Id {self.kwargs['pk']} ' })
        
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
    
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data}, status= status.HTTP_200_OK)
    
class get_comment(generics.ListAPIView):
    serializer_class = CommentSerializer
    
    
    def list(self, request, *args, **kwargs):
        post_id = self.kwargs.get('pk')
        try: 
            c = get_object_or_404(Post, pk = ObjectId(post_id))
            queryset = c.comment_set.all()
            if not queryset.exists():
                return Response({'detail': 'there is no comment exist for this comment'}, status= status.HTTP_200_OK)
            page = self.paginate_queryset(queryset)
            print('page',page)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response({'error': False, 'data': serializer.data}, status= status.HTTP_200_OK)
        
        except (ObjectDoesNotExist):
            return APIException({'error': True, 'msg': 'Post  not found' }, status= status.HTTP_404_NOT_FOUND)
        except (InvalidId):
            return APIException({'error': True, 'msg': f'Invalid Post id {post_id} ' }, status= status.HTTP_404_NOT_FOUND)
            
    
    
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
            raise APIException({'error': True, 'msg': 'comment  not found ' })
        
        except InvalidId:
            raise APIException({'error': True, 'msg': f'Invalid comment Id {self.kwargs['pk']} ' })
        
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
    
    
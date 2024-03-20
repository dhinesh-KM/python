from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from .models import product
from .serializer import ProductSerializer
from bson.objectid import ObjectId
from rest_framework import generics,permissions
import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class gp_product(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
        
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        response = {'error': False,'msg': 'Product created successfully','data': response.data}
        return Response(response, status=status.HTTP_201_CREATED)

        
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {'error': False, 'data': response.data}
        return Response(response, status= status.HTTP_200_OK)
  
    
  
class gud_product(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=ObjectId(self.kwargs['pk']))
            #self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            self.handle_not_found()
        
    def handle_not_found(self):
        response = {'error': True, 'msg': 'Product  not found' }
        return Response(response, status= status.HTTP_404_NOT_FOUND)
            
    def retrieve(self, request, *args, **kwargs):
        response =  super().retrieve(request, *args, **kwargs)
        if response.status_code == 404:
            return self.handle_not_found()
        else:
            response = {'error': False, 'data': response.data}
            return Response(response, status= status.HTTP_200_OK)
            
    def update(self, request, *args, **kwargs):
        response =  super().update(request, *args, **kwargs)
        response = {'error': False, 'data': response.data, 'msg': f'Product {response.data['name']} updated successfully' }
        return Response(response, status= status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        response =  super().destroy(request, *args, **kwargs)
        response = {'error': False, 'msg': f'Product  deleted successfully'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    
'''class Customlogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            
        })'''
'''logger = logging.getLogger(__name__)
class Customlogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        logger.info(f"User '{user.username}' successfully authenticated")

        token, created = Token.objects.get_or_create(user=user)
        logger.info(f"Token created for user '{user.username}'")

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
        })'''
        
    
        
        
        

'''@api_view(['GET','DELETE','PUT'])
def get_update_delete_product(request,pk):
    try:
        p = product.objects.get(pk=ObjectId(pk))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialize = ProductSerializer(p)
        return Response(serialize.data)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serialize = ProductSerializer(p,data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_204_NO_CONTENT)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def get_post_product(request):
    if request.method == 'GET':
        serialize = ProductSerializer(product.objects.all(),many=True)
        return Response(serialize.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'price': float(request.data.get('price')),
            'quantity': float(request.data.get('quantity')),
            'discount': int(request.data.get('discount'))
        }
        serialize = ProductSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)'''
    


    
    
    
    
    
            
            

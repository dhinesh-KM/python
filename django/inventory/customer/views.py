from rest_framework import generics,permissions
from .serializer import UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from bson.objectid import ObjectId

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class gp_user(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]
        
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        token = Token.objects.get(user = response).key
        response['token'] = token
        '''custom_user_obj_id = str(CustomUser.objects.get(id=response.data['id'])._id)  # Get the MongoDB _id
        response.data['object_id'] = custom_user_obj_id'''
        response = {'error': False,'msg': 'CustomUser created successfully','data': response.data}
        return Response(response, status=status.HTTP_201_CREATED)

        
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {'error': False, 'data': response.data}
        return Response(response, status= status.HTTP_200_OK)
  
    
  
class gud_user(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    
    
    def get_object(self):
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=self.kwargs['pk'])  #ObjectId(self.kwargs['pk']))
            #self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            self.handle_not_found()
        
    def handle_not_found(self):
        response = {'error': True, 'msg': 'CustomUser  not found' }
        return Response(response, status= status.HTTP_404_NOT_FOUND)
            
    def retrieve(self, request, *args, **kwargs):
        response =  super().retrieve(request, *args, **kwargs)
        custom_user_id = response.data.get('id', None)  # Get the default Django ID
        #custom_user_obj_id = str(CustomUser.objects.get(id=custom_user_id)._id)  
        print(response.data['id'])#,custom_user_obj_id)
        if response.status_code == 404:
            return self.handle_not_found()
        else:
            response = {'error': False, 'data': response.data}
            return Response(response, status= status.HTTP_200_OK)
            
    def update(self, request, *args, **kwargs):
        response =  super().update(request, *args, **kwargs)
        response = {'error': False, 'data': response.data, 'msg': f'CustomUser {response.data['username']} updated successfully' }
        return Response(response, status= status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        response =  super().destroy(request, *args, **kwargs)
        response = {'error': False, 'msg': f'CustomUser  deleted successfully'}
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